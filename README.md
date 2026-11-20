# Mkvplex Infinity

Android media-player project for ARM64 devices.

## Prepared artifacts

- Release tag: `v2.1.5-mkvplex.2`
- APK: `Mkvplex-Infinity-v2.1.5-build21500112-ARM64.apk`
- APK size: 112,450,363 bytes
- APK SHA-256: `b8acf93f90a7bef594d22191932639b3f758d452ff876854ccba71165a04d668`
- Full project archive: `Mkvplex-Infinity-v2.1.5-build21500112-FULL-SOURCE.zip`
- Full archive size: 299,925,165 bytes (about 286 MiB)
- Full archive SHA-256: `79de7f02c804b8f16a9d3eaf9a17299f3f8bd4a487822909691ce2de01eeaef2`

The full archive passed a ZIP integrity test.

## GitHub Release status

A draft release already exists at tag `v2.1.5-mkvplex.2`. It currently contains the ARM64 APK and the earlier Lite source archive. The 286 MiB full source archive has **not** yet been attached.

To attach the full archive:

1. Upload the full source ZIP to a file host that provides a direct HTTPS download URL accessible without login.
2. Open this repository's **Actions** tab.
3. Run **Attach full source archive to Mkvplex Infinity release**.
4. Paste the direct HTTPS URL into the `source_url` input.
5. The workflow verifies the SHA-256 checksum and uploads the full ZIP to the existing draft release.

The workflow does not publish the draft release; review it and publish it only after checking the project licensing, attribution, corresponding-source completeness, and third-party redistribution rights.

## Compatibility and validation

The APK has not been independently installed or tested on an Android device here. The source archive's ZIP integrity is verified, but a clean reproducible build has not been independently confirmed. Dolby Vision/Atmos playback depends on the device, codecs, and output route.

## Attribution and licensing

This project derives from the Mpv-infinity codebase. Preserve upstream copyright notices and applicable license terms. Review the included `LICENSE` and `THIRD_PARTY_LICENSES` before redistribution.
