# Shared source-track metadata fix (.5 to .6)

Version 2.1.5-mkvplex.6 / ARM64 build21500152. Reuse the existing owner-authorized .3/.4/.5 signing key.

The real Polyfin response captured during diagnosis contained 717 sources and 293,818 track references in 172,336,578 decompressed bytes. Only nine distinct projected track lists were present. The response exceeds the .5 128 MiB input cap, and counting every copied track against the retained budget also prevents it from loading safely. Both limits need to be handled without retaining the duplicated objects.

This is a common parser fix, with no title, source ID, server URL or account-specific branch. Identical projected track objects and lists are shared within one response. The domain-model parser preserves that sharing. Different indexes, types, codecs, languages, labels, external flags and delivery URLs remain distinct. Every source retains its original identity and order. No links or subtitle tracks are silently removed. Pooling tables are response-local.

The source response can stream up to 1 GiB of decompressed bytes while its estimated retained projection remains bounded at 32 MiB. Browse limits stay 32/8 MiB. Timeouts, cancellation and malformed-response checks remain active. Cache weighting counts shared lists once while retaining the existing global cache limits. This reduces client memory; it does not reduce the bytes sent by the server.

## Apply and rebuild

Starting from the original full source archive, apply POLYFIN_MEMORY_FIX.patch, STREAMING_MEMORY_FIX.patch and THREE_THOUSAND_LINKS.patch in that order. The new SHARED_TRACK_METADATA.patch then applies on top of .5. A .5 source checkout needs only this final delta.

Use JDK 17, Gradle 9.5.0, Android platforms 37.0 and 35 and build-tools 36.0.0. Build with customVersionCode=2150015, targetAbi=arm64-v8a, enableX86=false, and the existing previous_native.gradle/unshrunk_release.gradle init scripts. Use the verified .5 APK as native baseline; all 25 native engines and 220 bundled non-profile assets must remain identical. Sign with the existing private key, never a new key.

## Validation

See VALIDATION.json and SHA256SUMS.txt for the completed build and test results. Regression coverage includes the locally captured response, a lazily generated 3,000-link response with 420 subtitles per link, preservation of distinct subtitle URLs/indexes, response isolation, retained-budget enforcement after duplicate reuse, and bounded caching.

The actual response is private and is excluded from public source. The optional fixture test reads MKVPLEX_PROVIDER_FIXTURE when that local response snapshot is available. The captured snapshot has 717 links and 293,818 tracks. Other installations can run the generated regression fixtures without it.

Physical-device UI and playback validation remain pending. Automated parser tests do not establish that every title or every possible server payload has been tested.
