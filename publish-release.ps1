param(
  [string]$Apk = ".\\Mkvplex-Infinity-v2.1.5-build21500112-ARM64.apk",
  [string]$Source = ".\\Mkvplex-Infinity-v2.1.5-build21500112-SOURCE-ONLY-LITE.zip"
)

$ErrorActionPreference = "Stop"
$repo = "codex-ironman/Mkvplex-Infinity"
$tag = "v2.1.5-mkvplex.2"
$expectedApk = "b8acf93f90a7bef594d22191932639b3f758d452ff876854ccba71165a04d668"
$expectedSource = "d7b655012b2021e868be06f415dd1a6bd583ef538561d69e2356b49088d37486"

if (!(Get-Command gh -ErrorAction SilentlyContinue)) {
  throw "GitHub CLI is missing. Install from https://cli.github.com/ and run gh auth login."
}
gh auth status
if ($LASTEXITCODE -ne 0) { throw "Run gh auth login first." }
if (!(Test-Path -LiteralPath $Apk -PathType Leaf)) { throw "APK missing: $Apk" }
if (!(Test-Path -LiteralPath $Source -PathType Leaf)) { throw "Source ZIP missing: $Source" }
if ((Get-FileHash -Algorithm SHA256 -LiteralPath $Apk).Hash.ToLowerInvariant() -ne $expectedApk) {
  throw "APK checksum mismatch. Refusing to upload."
}
if ((Get-FileHash -Algorithm SHA256 -LiteralPath $Source).Hash.ToLowerInvariant() -ne $expectedSource) {
  throw "Source ZIP checksum mismatch. Refusing to upload."
}
$notes = @"
Mkvplex Infinity v2.1.5, build 21500112, Android ARM64.

Included:
- Original archived APK, SHA-256: $expectedApk
- Source-only archive, SHA-256: $expectedSource

This APK has not been independently installed or tested in this workflow.
Before publishing the draft, review third-party licenses, attribution, and
whether the source ZIP is the complete corresponding source for this APK.
"@
$notesFile = Join-Path $env:TEMP "mkvplex-infinity-release-notes.txt"
Set-Content -LiteralPath $notesFile -Encoding UTF8 -Value $notes
try {
  & gh release create $tag $Apk $Source --repo $repo --target main --title "Mkvplex Infinity v2.1.5 (ARM64)" --notes-file $notesFile --draft
  if ($LASTEXITCODE -ne 0) { throw "Release creation failed. Check gh output." }
  Write-Host "Draft release with APK and source files created. Review licensing and publish in GitHub."
} finally {
  Remove-Item -LiteralPath $notesFile -Force -ErrorAction SilentlyContinue
}
