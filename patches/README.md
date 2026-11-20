# Polyfin memory and link-loading fix

Build21500112 can exhaust its 512 MiB Java heap while the source chooser builds
language/search filters. The user stack ends in JellyfinSourceFilter.index.

The patch defers per-title version lists during home and library browsing,
discards unsolicited versions from lightweight item models, avoids retaining
combined lowercase strings for source search, and bounds the source cache by
estimated byte weight. The chooser builds its language index on a background
dispatcher. The progress bar follows isRefreshing through the ViewModel, so it
continues to show after usable links arrive and while more links are fetched.

Apply to the repository's original source ZIP from the repository root.

    unzip Mkvplex-Infinity-v2.1.5-build21500112-SOURCE-ONLY-LITE.zip -d work
    cd work/Mpv-infinity
    git apply --check ../../patches/POLYFIN_MEMORY_FIX.patch
    git apply ../../patches/POLYFIN_MEMORY_FIX.patch

The source ZIP's original SHA-256 is
d7b655012b2021e868be06f415dd1a6bd583ef538561d69e2356b49088d37486.

Validation completed with 83 JVM tests at a 64 MiB heap. The original filter
fails the same synthetic large-label regression with OutOfMemoryError. Tests
compiled the production client, parser, loader, request coalescing, cache and
filter using Kotlin 2.4.10, OkHttp 5.5.0, Okio 3.18.1, kotlinx.serialization
1.11.0 and coroutines 1.10.2. Android/application classes used minimal test stubs.

Android APK and Compose UI compilation and physical-device testing remain pending.
The live server authentication attempt returned HTTP 403. The stress test
establishes the allocation regression, without measuring the phone's full heap.

Restore omitted AARs, native dependencies, fonts and the Gradle wrapper JAR
before rebuilding this Lite source. Sign an update with the existing key and
use a versionCode greater than 21500112. The original binary and release helper
continue to refer to the original build. No rebuilt APK is included.
