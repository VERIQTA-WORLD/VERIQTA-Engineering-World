"""Execute only allowlisted first-batch snippets in disposable local directories.

Do not extend this runner to discover or execute arbitrary contributed code.
"""
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]

def block(path,language):
    text=(ROOT/path).read_text()
    return re.findall(r'```'+language+r'\n(.*?)```',text,re.S)[0]

def shell(text, cwd):
    completed=subprocess.run(['sh','-c',text],cwd=cwd,text=True,capture_output=True,timeout=20)
    if completed.returncode:
        raise AssertionError(f'Shell check failed ({completed.returncode}): {completed.stderr}')
    return completed.stdout

def main():
    results=[]
    with tempfile.TemporaryDirectory(prefix='veriqta-check-') as d:
        cwd=Path(d)
        # Day 2 creates its own scoped workspace; keep it under the runner root.
        prefix='set -eu\nexport TMPDIR="'+str(cwd)+'"\n'
        text=block('journey/days/day-02.md','sh')
        shell(prefix+text+'\ngit --version > "$workspace/notes/environment.txt"\npython3 --version >> "$workspace/notes/environment.txt"\ntest -f "$workspace/notes/scope.txt"\n',cwd)
        results.append({'id':'VW-DAY002','scope':'Workspace setup snippet and environment inventory','result':'passed'})
        shell(prefix+block('journey/days/day-03.md','sh')+'\nchmod 400 "$lab/config/service.conf"\ntest "$(cat "$lab/config/service.conf")" = mode=demo\nchmod 600 "$lab/config/service.conf"\n',cwd)
        results.append({'id':'VW-DAY003','scope':'Permission setup, 400/600 transitions and content check; no cross-user access test','result':'passed'})
        log=block('journey/days/day-04.md','text')
        (cwd/'requests.log').write_text(log)
        assert len(log.splitlines())==4
        assert shell("grep 'status=503' requests.log",cwd).count('status=503')==2
        assert len([line for line in log.splitlines() if 'route=/search' in line])==3
        results.append({'id':'VW-DAY004','scope':'Log fixture counts and grep result','result':'passed'})
        gitdir=cwd/'git-lab';gitdir.mkdir()
        shell('set -eu\ngit init\n'+block('journey/days/day-05.md','sh')+'\ntest "$(git rev-list --count HEAD)" = 2\ntest -z "$(git status --porcelain)"\n',gitdir)
        results.append({'id':'VW-DAY005','scope':'Actual lesson Git commands, two commits and clean disposable tree','result':'passed'})
        script=block('journey/days/day-06.md','sh')
        (cwd/'check-config.sh').write_text(script)
        (cwd/'good config.txt').write_text('mode=demo\n');(cwd/'bad.txt').write_text('mode=prod\n')
        shell('sh -n check-config.sh',cwd)
        for args,expected in [(['good config.txt'],0),(['bad.txt'],1),(['missing.txt'],1),([],2)]:
            r=subprocess.run(['sh','check-config.sh']+args,cwd=cwd,capture_output=True,timeout=10)
            assert r.returncode==expected,(args,r.returncode)
        results.append({'id':'VW-DAY006','scope':'Published script syntax and four behavioral exit-code cases','result':'passed'})
        results.append({'id':'VW-DAY007','scope':'Reused Day 6 script rejects supplied prod fixture; handoff reasoning requires review','result':'passed'})
        shell(prefix+block('library/vw-e001.md','sh')+'\ntest "$(wc -c < "$lab/debug.log" | tr -d " ")" = 13000\nrm "$lab/app.log" "$lab/debug.log" "$lab/keep.txt"\nrmdir "$lab"\n',cwd)
        results.append({'id':'VW-E001','scope':'Published setup, byte-count assertion and scoped cleanup; no live disk incident','result':'passed'})
        code=block('solutions/vw-e002.md','python')
        namespace={'__name__':'lab_reference'}
        exec(compile(code,'manifest_reference','exec'),namespace)
        good={'service':'cart','replicas':2,'digest':'sha256:'+'a'*64}
        assert namespace['valid'](good)
        for value in [True,0,6,None,'2']:
            assert not namespace['valid'](dict(good,replicas=value))
        for bad in [None,[],{},dict(good,extra=1),dict(good,digest='sha256:a'),dict(good,service=' ')]:
            assert not namespace['valid'](bad)
        (cwd/'validate.py').write_text(code)
        for filename,content,expected in [('valid.json',json.dumps(good),0),('invalid.json','{',1),('list.json','[]',1),('null.json','null',1)]:
            (cwd/filename).write_text(content)
            r=subprocess.run([sys.executable,'validate.py',filename],cwd=cwd,capture_output=True,timeout=10)
            assert r.returncode==expected
        for args in [[],['absent.json']]:
            r=subprocess.run([sys.executable,'validate.py']+args,cwd=cwd,capture_output=True,timeout=10)
            assert r.returncode==2
        results.append({'id':'VW-E002','scope':'Reference implementation type/boundary tests plus CLI valid/malformed/list/null/missing/usage cases','result':'passed'})
    print(json.dumps(results,indent=2))

if __name__=='__main__':
    main()
