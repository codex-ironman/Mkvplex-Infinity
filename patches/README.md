# Polyfin memory and link-loading fix

The source chooser in build21500112 could exhaust its Android heap while
indexing provider versions. The progress indicator also stopped after initial
links arrived, even while the provider was still fetching more links.

This patch defers source lists during browsing, discards unsolicited source
lists from lightweight models, avoids retained combined lowercase search text,
and bounds cached metadata by estimated byte weight. Language indexing runs
on a background dispatcher. The progress bar follows refresh and indexing
state, while received links remain selectable. Cancelling the chooser also
prevents a newly freed check slot from starting another waiting probe.

The release version is 2.1.5-mkvplex.3, ARM64 versionCode 21500122.

## Validation

- Android debug and release Kotlin/Compose compilation passed.
- Android unit tests: 287 passed, 2 skipped, no failures or errors.
- Targeted JVM suite: 83 tests passed with a 64 MiB heap. The original filter
  fails the same synthetic large-label allocation regression with OutOfMemoryError.
- The cancellation test group passed 100 repetitions, totaling 400 checks.
- Release APK ZIP integrity, package/version, ARM64-only ABI, non-debuggable
  manifest and 16 KiB ZIP alignment passed.
- All 25 native libraries and 219 bundled non-profile assets are byte-identical
  to original build21500112. The Kotlin/Java code was rebuilt; native engines
  were reused from the verified APK and supplied AARs.
- Physical-device playback and the phone's complete heap behavior remain
  unverified. The live Polyfin authentication attempt returned HTTP 403.

## Rebuild

The new build21500122 FULL-SOURCE ZIP already includes this patch. Skip the git-apply commands below when using that archive; they apply only to the original build21500112 source.

Use the supplied complete source archive, whose SHA256 is
`79de7f02c804b8f16a9d3eaf9a17299f3f8bd4a487822909691ce2de01eeaef2`.
The repository's Lite ZIP can receive this patch, but lacks AARs, native
dependencies, fonts and the Gradle wrapper JAR needed for the Android build.

Inside the extracted full archive root, apply the patch to Mpv-infinity:

```bash
git -C Mpv-infinity apply --check /path/to/patches/POLYFIN_MEMORY_FIX.patch
git -C Mpv-infinity apply /path/to/patches/POLYFIN_MEMORY_FIX.patch
```

For the same native selection as the verified build, stage the three unchanged
CMake outputs from original build21500112 using Python 3.11 or newer. The helper
checks the entire original APK SHA256 before extracting any files.

```bash
python3 /path/to/patches/prepare_native_build21500112.py /path/to/original-build21500112.apk "$PWD/native"
export MKVPLEX_NATIVE_ROOT="$PWD/native"
cd Mpv-infinity
./gradlew :app:testStandardDebugUnitTest :app:assembleStandardRelease \
  -PtargetAbi=arm64-v8a -PenableX86=false \
  -PcustomApplicationId=app.infinity.mpvz.mkvplex -PcustomVersionCode=2150012 \
  --no-configuration-cache --max-workers=1 \
  -I ../build-tools/previous_native.gradle -I ../build-tools/unshrunk_release.gradle
```

Use JDK 17, Android SDK platforms 37.0 and 35, and build-tools 36.0.0.
This build keeps the original release's unshrunk packaging configuration.

To match its established native packaging, run the supplied packager after
Gradle. It preserves all original native engines, checks bundled assets and
aligns the resulting unsigned APK to 16 KiB. In this build, libquickjs.so and
libtorrent4j.so from dependency packaging differed from the previous binary;
their original verified versions were retained.

```bash
python3 /path/to/patches/package_native_build21500112.py \
  /path/to/original-build21500112.apk \
  app/build/outputs/apk/standard/release/app-standard-arm64-v8a-release-unsigned.apk \
  /path/to/native-preserved-unsigned.apk "$ANDROID_HOME"
```

## Signing and publication

The owner authorized a new release key on 20 November 2026 because the previous
private signing key was unavailable. The fixed ARM64 APK is now signed and
verified with v1, v2 and v3 schemes and 16 KiB alignment.

Uninstall the old build21500112 before installing this release. This can erase
local settings and saved sign-ins. Future releases must reuse this new key.

- APK: `Mkvplex-Infinity-v2.1.5-mkvplex.3-build21500122-ARM64.apk`
- APK SHA256: `9e04eb72497a5bd8c7e7838a475d3f6ff7f7360e9cd117a04188a6fe8f44d944`
- New certificate SHA256: `f786eb6650fa04cb86599cd6e85233ffc794347c5763fb5019796df0d028f535`
- Android unit tests: 287 passed, 2 skipped.
- Physical-device playback remains unverified.

The private key and password were saved separately for the owner and are
excluded from the source archive and GitHub release assets. The public
certificate and signed-build validation are in
`releases/v2.1.5-mkvplex.3/`.

To sign a future native-preserved unsigned APK, use the owner's saved private
backup and the same alias. The PKCS12 key password is the store password.

```bash
apksigner sign --ks /private/mkvplex-infinity-release.p12 \
  --ks-key-alias mkvplex-infinity-release \
  --ks-pass file:/private/store-password.txt \
  --out /path/to/signed.apk /path/to/native-preserved-unsigned.apk
apksigner verify --verbose --print-certs /path/to/signed.apk
```

The older .2 draft predates these fixes. FIX_VALIDATION.json records the
unsigned compilation checkpoint; releases/v2.1.5-mkvplex.3/RELEASE_VALIDATION.json
records the signed build.
