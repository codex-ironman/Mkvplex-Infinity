Mkvplex Infinity 2.1.5-mkvplex.3 — ARM64 build21500122

- Reduces retained source/filter metadata to address the reported Polyfin chooser OutOfMemoryError.
- Keeps progress visible while additional links and language filters load.
- Prevents waiting link probes from starting after chooser cancellation.
- Android unit tests: 287 passed, 2 skipped. Targeted allocation tests: 83 passed at 64 MiB. Cancellation suite: 400 repeated checks passed.
- All 25 native libraries and 219 bundled non-profile assets retain the previous build's bytes.

This release uses a NEW signing key, as requested by the owner. Uninstall the old build21500112 first, then install this APK. Uninstalling can erase local settings and saved sign-ins. Subsequent releases will reuse this new key.

APK SHA256: 9e04eb72497a5bd8c7e7838a475d3f6ff7f7360e9cd117a04188a6fe8f44d944
Signing certificate SHA256: f786eb6650fa04cb86599cd6e85233ffc794347c5763fb5019796df0d028f535
Source patch and rebuild instructions: https://github.com/codex-ironman/Mkvplex-Infinity/tree/main/patches

Android compilation and signature checks passed. Physical-device playback and the phone's complete heap behavior remain unverified. The live Polyfin authentication attempt returned HTTP 403.
