# Compact metadata and 3,000-link chooser

This patch is a four-file delta from build21500132 (.4) to build21500142 (.5). Apply it after the existing .4 streaming-memory patch; do not replace or skip that earlier patch.

```sh
git apply /path/to/patches/THREE_THOUSAND_LINKS.patch
```

Patch SHA256: 5d913f2a69a9cd8865790f0e214fcebdc42be8ce4a33772c278c72432765c416

# 3,000-link candidate .5

Version 2.1.5-mkvplex.5, ARM64 build21500142. Signed with the same certificate as .3/.4; those installations can update without uninstalling.

Large link responses now retain only source identity, playback path, video/audio information and subtitle delivery information. Duplicate per-source catalog fields are skipped while streaming. Source responses allow up to 128 MiB of decompressed input and a 32 MiB estimated retained metadata budget; browse responses keep the smaller limits. Oversized or malformed responses still fail safely.

The source chooser shows 100 matches initially. “Show 100 more” adds another batch. Search and language filters use the entire fetched source list, including links beyond the first batch. Keep the advanced fetched-link limit at 0 (All) to load more than 500 links; an explicitly selected limit still applies.

Android compilation passed. 311 unit tests passed, 2 skipped. All 58 stress tests passed with a 64 MiB Java heap, including generated 1,000-, 2,000- and 3,000-link responses with video, audio and external subtitles, final-source search and ignored duplicated catalog metadata.

APK SHA256: 34a673fb619c529e3193e374678c260626e792da86fac18844a4edd8a8bede56

The APK signature passes v1/v2/v3 verification and 16 KiB alignment checks. All 25 native libraries remain identical to the prior signed baseline. Private signing material is excluded.

## Remaining device validation

The owner's .4 screenshot for The Odyssey showed the metadata guard rejecting its response. These automated tests do not establish that the exact server response or OnePlus Android 16 flow is fixed. Repeat that flow with this signed .5 candidate and check link loading, full-list search, subtitle selection and playback. A public APK release has not been uploaded or published.

