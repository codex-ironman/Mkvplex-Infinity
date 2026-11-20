Mkvplex Infinity 2.1.5-mkvplex.4 — build21500132 (ARM64 phone-test candidate)

Build .3 still exhausted the Android heap when many links were fetched. This
candidate streams/project metadata, bounds oversized responses and source text,
and bounds/cancels artwork loading. It also adds sanitized MkvMemory counters.

310 unit tests passed, 2 skipped. All 57 stress tests passed with a 64 MiB heap,
including a 1000-link list and a generated 24 MiB unused provider field.

This APK uses the SAME signing key as .3 and can update that installation.
No additional uninstall is needed. All 25 native engines and 219 existing
bundled assets are retained; one Gson license asset was added.

APK SHA256: ce8ec0b95e043d257bbcd8e67934fd2d735b9e28e479f6c2ddda5c502e055894
Certificate SHA256: f786eb6650fa04cb86599cd6e85233ffc794347c5763fb5019796df0d028f535

Phone validation of the reported many-link OOM remains pending. This is a
candidate for repeating that exact device flow, not a confirmed device fix.
