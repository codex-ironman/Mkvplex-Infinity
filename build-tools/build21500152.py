"""Build the already-patched .6 application with its verified prebuilt ARM64 inputs."""
import os, pathlib, subprocess, sys, urllib.parse

tools = pathlib.Path(__file__).resolve().parent
project = tools.parent / 'Mpv-infinity'
cache = tools / 'gradle-user'
cache.mkdir(exist_ok=True)
settings = ['org.gradle.jvmargs=-Xmx4g -XX:ActiveProcessorCount=2 -Dfile.encoding=UTF-8',
            'kotlin.compiler.execution.strategy=in-process']
proxy = urllib.parse.urlparse(os.environ.get('HTTPS_PROXY', ''))
if proxy.hostname:
    settings += [f'systemProp.{scheme}.proxyHost={proxy.hostname}' for scheme in ('http', 'https')]
    settings += [f'systemProp.{scheme}.proxyPort={proxy.port or 80}' for scheme in ('http', 'https')]
(cache / 'gradle.properties').write_text('\n'.join(settings) + '\n')
env = dict(os.environ, GRADLE_USER_HOME=str(cache), MKVPLEX_NATIVE_ROOT=str(tools / 'native'))
tasks = sys.argv[1:] or [':app:testStandardDebugUnitTest', ':app:memoryStressTest', ':app:assembleStandardRelease']
command = ['bash', str(project / 'gradlew'), *tasks,
           '-PtargetAbi=arm64-v8a', '-PenableX86=false', '-PcustomApplicationId=app.infinity.mpvz.mkvplex',
           '-PcustomVersionCode=2150015', '-Pkotlin.compiler.execution.strategy=in-process',
           '-Pksp.incremental=false', '-Pkotlin.incremental=false',
           '--no-configuration-cache', '--no-daemon', '--max-workers=1', '--console=plain',
           '-I', str(tools / 'previous_native.gradle'), '-I', str(tools / 'unshrunk_release.gradle'),
           '-I', str(tools / 'memory_stress.gradle')]
raise SystemExit(subprocess.run(command, cwd=project, env=env).returncode)
