# Mkvplex Infinity .6 — application source and build inputs

Version: 2.1.5-mkvplex.6. Package: app.infinity.mpvz.mkvplex. ARM64 versionCode: 21500152.

Mpv-infinity/ already contains all .3, .4, .5 and .6 application changes. Do not apply the reference patches again. Kotlin/Java/Compose application source, application C++ source, resources, fonts, bundled AARs, licenses and the Gradle wrapper are included. The supplied AARs and .so files are compiled dependencies, not editable source for every third-party engine. Preserve upstream license and attribution files.

## Build

Install Python 3, JDK 17 and Android SDK platforms 37.0 and 35, plus build-tools 36.0.0. Gradle 9.5.0 and Maven dependencies are downloaded by the wrapper on first build. Use Linux/macOS or a compatible bash environment, with JAVA_HOME and ANDROID_HOME set to your installations. Allow several GiB of disk and memory for a first build.

From the extracted archive root:

```sh
python3 build-tools/build21500152.py
```

This runs the unit suite, the 64 MiB stress suite and the unshrunk ARM64 release build. The three prebuilt CMake outputs under build-tools/native/ are byte-identical to the verified .5/.6 APKs; the init script stages them without rebuilding native engines. Other native dependencies come from the bundled AARs/Maven dependencies. The player engine source/configuration was not changed by the .6 metadata fix.

Unsigned output:

```text
Mpv-infinity/app/build/outputs/apk/standard/release/app-standard-arm64-v8a-release-unsigned.apk
```

Before distributing a rebuilt APK, retain and verify all 25 native library bytes against the signed .6 baseline listed in release/BASELINE_INPUTS.json. Dependency packaging previously produced different libquickjs.so/libtorrent4j.so bytes; the delivered signed APK retained the baseline versions. Run zipalign with 16 KiB page alignment after final packaging, then sign using the existing owner key and alias mkvplex-infinity-release. The private keystore/password are deliberately excluded; keep the previously saved private backup separately.

## Validation and private fixture

The delivered .6 build passed compilation, 316 unit tests (2 skipped) and 74 stress tests with a 64 MiB heap. release/VALIDATION.json pins its APK and source-delta checksums. The exact private server response was replayed locally: 717 links, 293,818 track references and nine distinct projected track lists. It is excluded because server responses can contain account URLs. The optional test reads MKVPLEX_PROVIDER_FIXTURE when that exact local snapshot is available; without it, that one additional test skips. Generated 3,000-link/420-subtitle tests remain available without private data.

Physical-device UI/playback retesting remains pending. The full app source and memory fix are included; these automated results do not mean every possible server response has been tested.

Source origin archive SHA256: 79de7f02c804b8f16a9d3eaf9a17299f3f8bd4a487822909691ce2de01eeaef2.
GitHub source delta/validation commit: f33fe21718ec6d7d9e6fd9433f905b563c8130ec.
All project file hashes are recorded in SOURCE_FILE_MANIFEST.json.
