"""Preserve original build21500112 native engines in a newly compiled ARM64 APK."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('previous_apk', type=Path)
parser.add_argument('fresh_apk', type=Path)
parser.add_argument('output_apk', type=Path)
parser.add_argument('android_sdk', type=Path)
args = parser.parse_args()
with args.previous_apk.open('rb') as stream:
    if hashlib.file_digest(stream, 'sha256').hexdigest() != 'b8acf93f90a7bef594d22191932639b3f758d452ff876854ccba71165a04d668':
        raise SystemExit('Original APK SHA256 mismatch; nothing packaged.')
output = args.output_apk.resolve()
output.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(args.previous_apk) as old, zipfile.ZipFile(args.fresh_apk) as new:
    assert new.testzip() is None, 'Invalid new APK ZIP'
    libs = {n for n in old.namelist() if n.startswith('lib/') and n.endswith('.so')}
    assert len(libs) == 25 and libs == {n for n in new.namelist() if n.startswith('lib/') and n.endswith('.so')}
    assets = {n for n in old.namelist() if n.startswith('assets/') and not n.startswith('assets/dexopt/') and not n.endswith('/')}
    assert len(assets) == 219 and assets == {n for n in new.namelist() if n.startswith('assets/') and not n.startswith('assets/dexopt/') and not n.endswith('/')}
    assert all(old.read(n) == new.read(n) for n in assets), 'Unexpected bundled-asset changes'
    normalized = sorted(n for n in libs if old.read(n) != new.read(n))
    with tempfile.TemporaryDirectory(prefix='polyfin-package-', dir=output.parent) as directory:
        preserved = Path(directory) / 'preserved.apk'
        aligned = Path(directory) / 'aligned.apk'
        with zipfile.ZipFile(preserved, 'w') as packed:
            for entry in new.infolist():
                packed.writestr(entry, old.read(entry.filename) if entry.filename in libs else new.read(entry.filename))
        subprocess.run([str(args.android_sdk / 'build-tools/36.0.0/zipalign'), '-P', '16', '-f', '4', str(preserved), str(aligned)], check=True)
        shutil.copyfile(aligned, output)
with output.open('rb') as stream:
    digest = hashlib.file_digest(stream, 'sha256').hexdigest()
print(json.dumps({'unsigned_apk': str(output), 'sha256': digest, 'preserved_libraries': len(libs), 'normalized_from_original': normalized}, indent=2))
