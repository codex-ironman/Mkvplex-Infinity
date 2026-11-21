# Mkvplex Infinity

> **Release paused:** build21500122 (`2.1.5-mkvplex.3`) still exhausted the Android heap during the owner's large-link test. Its earlier unit-test pass did not establish a complete device fix. Do not publish it as the corrected memory release. Candidate `.6` shares repeated track metadata across every source response. The actual 164 MiB server snapshot and 3,000-link regression pass with a 64 MiB heap; phone UI/playback retesting remains pending.

Android media-player project for ARM64 devices.

## Current shared-metadata candidate .6

`2.1.5-mkvplex.6` / ARM64 build `21500152` fixes repeated subtitle/track
metadata in the common parser, with no title-specific branches. The captured
Polyfin response had **717 links and 293,818 track references**, but only
**nine distinct projected track lists**, in **172,336,578 bytes**.

Identical track objects/lists are shared during streaming and model conversion.
Source identity/order, all tracks, distinct subtitle URLs and indexes are preserved.
Input work is bounded separately from the retained metadata budget. The source
chooser still shows batches of 100 and searches the complete fetched list.

**316 unit tests passed, 2 skipped; 74 stress tests passed with a 64 MiB heap.**
This includes the actual captured response and a generated **3,000-link response
with 420 subtitles per link**. The signed APK passes package/version, v1/v2/v3
signature and 16 KiB alignment checks; all 25 native libraries and 220 bundled
non-profile assets match .5. It uses the same signing key as .3/.4/.5.

[Source delta and build/retest notes](patches/SHARED_TRACK_METADATA.md) ·
[Signed candidate validation/checksums](releases/v2.1.5-mkvplex.6/)

The APK is prepared for the owner's phone retest. Physical-device UI/playback
is not yet verified, and a .6 APK has not been uploaded/published as a GitHub
Release. The .5 tests did not cover the repeated-hundreds-of-subtitles payload
that caused the owner's metadata-limit error.

## Previous 3,000-link candidate .5

`2.1.5-mkvplex.5` / ARM64 build `21500142` uses the same signing key as .3/.4.
It retains compact playback metadata and shows matches in batches of 100; search
and language filters cover all fetched links. Use fetched-link limit **0 (All)**
for 1,000–3,000 links.

Android compilation passed: **311 unit tests passed, 2 skipped**, and **58 stress
tests passed with a 64 MiB heap**, including 1,000-, 2,000- and 3,000-link fixtures
with audio/subtitles and final-source search.

[Source delta and retest instructions](patches/THREE_THOUSAND_LINKS.md) ·
[Signed candidate validation/checksums](releases/v2.1.5-mkvplex.5/)

The owner's .4 test displayed “too much metadata” for The Odyssey. The .5 APK is
prepared for that phone retest; the real-device fix is not yet confirmed.
APK upload/publication to GitHub remains pending.

## Previous memory test candidate .4

`2.1.5-mkvplex.4` / ARM64 build `21500132` is signed with the same key as .3.
It can update that installation. Android compilation passed; **310 unit tests
passed, 2 skipped**, and **57 stress tests passed with a 64 MiB heap**. Cases
include 1000 links and a generated 24 MiB ignored provider field.

[Source patch and retest instructions](patches/STREAMING_MEMORY_FIX.md) ·
[Signed candidate validation/checksums](releases/v2.1.5-mkvplex.4/)

The candidate APK and full source are prepared for the owner's phone retest.
The device OOM is **not yet confirmed resolved**; public release remains paused.

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



