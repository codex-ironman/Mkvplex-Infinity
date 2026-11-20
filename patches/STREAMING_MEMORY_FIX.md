# Build21500132 memory candidate after the .3 device crash

Build21500122 still exhausted the phone's 512 MiB Java heap. Its final failed
allocation was in the Compose frame clock; that stack does not identify the
retained objects. The owner observed that the crash follows fetching many links.
The older filter-only regression tests did not reproduce the whole phone workload.

This patch addresses concrete remaining allocation paths:

- Jellyfin metadata is read through Gson's streaming JsonReader. Unused fields
  and unsolicited browse MediaSources are skipped before becoming JSON objects.
  Decoded metadata parsing is serialized across clients; input is bounded to
  32 MiB decompressed bytes and the retained projection to an estimated 8 MiB.
  Oversized responses fail explicitly and do not trigger automatic link retries.
  Normal link lists are not silently truncated.
- Source labels passed to Compose are limited to 1024 characters and 3 lines;
  descriptions are built incrementally up to 1536 characters and 4 lines.
  Original source IDs and metadata remain available for selection and search.
  Search no longer joins full track descriptions into another large string.
- Image sampling bounds both dimensions and total pixels. Cards use at most
  393216 pixels and hero artwork at most 1327104 pixels. The former 2048-pixel
  loop could leave a 4095-pixel image unsampled.
- Image loads share active readers, allow two concurrent decodes, and cancel
  queued/in-flight coroutine work when the final viewer leaves. HTTP images
  stream through a 16 MiB limit into a temporary disk file, avoiding body.bytes().
  Image memory caches are cleared on Android memory-trim callbacks.
- Sanitized MkvMemory logs report stage/counts, bitmap dimensions and heap usage.
  No URLs, account identifiers, tokens or response text are logged.

The candidate version is 2.1.5-mkvplex.4, ARM64 versionCode 21500132. It must
reuse the owner's newly saved .3 signing key. The private key is not in this patch.

## Apply

Use the complete build21500122 source (the .3 FULL-SOURCE ZIP), then run inside
Mpv-infinity:

```bash
git apply --check /path/to/STREAMING_MEMORY_FIX.patch
git apply /path/to/STREAMING_MEMORY_FIX.patch
```

When starting from the original build21500112 source, apply
POLYFIN_MEMORY_FIX.patch first, then this patch. The Lite archive still lacks
the native/AAR/font inputs needed for the complete Android build.

Gson 2.15.0 is added for streaming projection. Its Apache-2.0 license is bundled
under app/src/main/assets/licenses/ and its source is https://github.com/google/gson.

## Validation status

Android compilation and full/stress tests are in progress. New regression cases
cover 1000 retained links, a generated 24 MiB ignored provider field, byte/retained
budgets, sampling bounds, shared-load cancellation, and long source labels.
The targeted stress run uses a 64 MiB Java heap.

The phone's actual retained heap has not been captured. A passing synthetic test
does not establish that all causes of the reported device OOM are resolved.
The .3 release is paused, and this candidate needs the same many-link phone test.
