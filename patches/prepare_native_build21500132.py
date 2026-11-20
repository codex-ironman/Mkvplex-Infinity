"""Stage unchanged ARM64 CMake outputs from the verified original custom APK."""
import argparse
import hashlib
from pathlib import Path
import zipfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('apk', type=Path)
parser.add_argument('output', type=Path)
args = parser.parse_args()
expected = 'ce8ec0b95e043d257bbcd8e67934fd2d735b9e28e479f6c2ddda5c502e055894'
with args.apk.open('rb') as stream:
    actual = hashlib.file_digest(stream, 'sha256').hexdigest()
if actual != expected:
    raise SystemExit('APK SHA256 does not match original build21500132; nothing extracted.')
entries = {
    'lib/arm64-v8a/libqjs.so': 'app/arm64-v8a/libqjs.so',
    'lib/arm64-v8a/libytdl.so': 'app/arm64-v8a/libytdl.so',
    'lib/arm64-v8a/libmedia3_subtitle_libass.so': 'subtitle-libass/arm64-v8a/libmedia3_subtitle_libass.so',
}
with zipfile.ZipFile(args.apk) as archive:
    payloads = [(args.output / target, archive.read(name)) for name, target in entries.items()]
for target, data in payloads:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
print('Staged 3 verified ARM64 native libraries.')

