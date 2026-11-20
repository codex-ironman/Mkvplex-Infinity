# Mkvplex Infinity

> **Release paused:** build21500122 (`2.1.5-mkvplex.3`) still exhausted the Android heap during the owner's large-link test. Its earlier unit-test pass did not establish a complete device fix. Do not publish it as the corrected memory release. Candidate `.4` is being validated with streamed metadata, bounded artwork and large-response stress tests; phone validation remains pending.

Android media-player project for ARM64 devices.

## Polyfin fix — signed build prepared

Version `2.1.5-mkvplex.3` / ARM64 build `21500122` includes the chooser memory,
link-loading progress and cancellation fixes. Android unit tests: **287 passed,
2 skipped**. The signed APK passed v1/v2/v3 signature verification and 16 KiB
alignment checks.

This release uses a **new owner-authorized signing key**. Uninstall the old
build21500112 before installation; local settings/sign-ins may be removed.
Subsequent updates will reuse the new key.

- APK SHA256: `9e04eb72497a5bd8c7e7838a475d3f6ff7f7360e9cd117a04188a6fe8f44d944`
- Certificate SHA256: `f786eb6650fa04cb86599cd6e85233ffc794347c5763fb5019796df0d028f535`
- [Signed build validation and public certificate](releases/v2.1.5-mkvplex.3/)
- [Source patch and rebuild instructions](patches/README.md)

The fixed signed APK and private recovery backup are prepared. GitHub release
upload is pending. The private key/password are excluded from public artifacts.
The older .2 draft below predates these fixes.

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

The APK has not been independently installed or tested on an Android device here. The Polyfin fix has passed Android compilation and unit tests using the complete source and verified prebuilt native binaries. Dolby Vision/Atmos playback depends on the device, codecs, and output route.

## Attribution and licensing

This project derives from the Mpv-infinity codebase. Preserve upstream copyright notices and applicable license terms. Review the included `LICENSE` and `THIRD_PARTY_LICENSES` before redistribution.


