"""Dependency-free repository checks. Static evidence only; never runs content code."""
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
STATUS = {'planned', 'draft', 'reviewed'}
TYPES = {'concept','exercise','incident','ai-exercise','decision','project'}
LAB_SECTIONS = {'mission','outcomes','environment and scope','prerequisite checks','setup','concepts','tasks','expected observations','verification','troubleshooting','cleanup','reflection'}

def headings(text):
    """GitHub-style heading slugs for this repository's plain-text headings."""
    counts, result = {}, set()
    clean = re.sub(r'```.*?```', '', text, flags=re.S)
    for heading in re.findall(r'^#{1,6} (.+)$', clean, re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        slug = re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-')
        n = counts.get(slug,0)
        result.add(slug if not n else f'{slug}-{n}')
        counts[slug] = n+1
    return result

def record_errors(records, day_records=False):
    errors, ids = [], {x.get('id') for x in records}
    seen = set()
    required = {'id','title','topic','status','path','prerequisites','estimated_minutes','execution'}
    if not day_records:
        required |= {'tags','type','difficulty','environment','cost','versions','sources','sources_checked','solution'}
    for x in records:
        ident = x.get('id','<missing>')
        if required - set(x):
            errors.append(f'{ident}: missing metadata {sorted(required-set(x))}')
        if ident in seen:
            errors.append(f'{ident}: duplicate ID')
        seen.add(ident)
        if not re.fullmatch(r'VW-(?:[CEAIDP]\d{3}|DAY\d{3})',ident):
            errors.append(f'{ident}: invalid stable ID')
        if x.get('status') not in STATUS:
            errors.append(f'{ident}: invalid editorial status')
        if x.get('status') == 'reviewed' and (not x.get('reviewer') or not x.get('review_date')):
            errors.append(f'{ident}: reviewed without reviewer/date')
        if x.get('status') == 'planned' and x.get('path') is not None:
            errors.append(f'{ident}: planned item has lesson path')
        if x.get('status') != 'planned' and not x.get('path'):
            errors.append(f'{ident}: authored item needs a path')
        if type(x.get('estimated_minutes')) is not int or x['estimated_minutes'] <= 0:
            errors.append(f'{ident}: invalid estimated time')
        for prerequisite in x.get('prerequisites',[]):
            if prerequisite not in ids:
                errors.append(f'{ident}: invalid prerequisite {prerequisite}')
        if not day_records:
            if x.get('type') not in TYPES:
                errors.append(f'{ident}: invalid type')
            if x.get('difficulty') not in {'beginner','intermediate','advanced'}:
                errors.append(f'{ident}: invalid difficulty')
            for key in ['environment','cost','versions','topic','title']:
                if not isinstance(x.get(key),str) or not x[key].strip():
                    errors.append(f'{ident}: empty {key}')
            if not x.get('sources') or not all(urlsplit(s).scheme=='https' for s in x.get('sources',[])):
                errors.append(f'{ident}: invalid sources')
            try:
                date.fromisoformat(x.get('sources_checked',''))
            except ValueError:
                errors.append(f'{ident}: invalid source date')
        execution = x.get('execution',{})
        if execution.get('status') not in {'not-run','passed','failed','partial'}:
            errors.append(f'{ident}: invalid execution status')
        if execution.get('status') != 'not-run' and not all(execution.get(k) for k in ['environment','date','result']):
            errors.append(f'{ident}: execution evidence missing')
    return errors

def markdown_errors(root, path):
    text = path.read_text()
    rel = path.relative_to(root)
    errors = []
    # Fences excluded so fixture examples aren't treated as headings/links.
    clean = re.sub(r'```.*?```','',text,flags=re.S)
    if text.count('```') % 2:
        errors.append(f'{rel}: unbalanced code fence')
    h1 = re.findall(r'^# .+$',clean,re.M)
    if len(h1) != 1:
        errors.append(f'{rel}: expected one H1')
    previous = 0
    for hashes in re.findall(r'^(#{1,6}) ',clean,re.M):
        if len(hashes) > previous+1:
            errors.append(f'{rel}: skipped heading level')
        previous=len(hashes)
    if any(line.rstrip()!=line for line in text.splitlines()):
        errors.append(f'{rel}: trailing whitespace')
    links = re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',clean)
    links += re.findall(r'(?:src|href)="([^"]+)"',clean)
    for link in links:
        parsed = urlsplit(link.strip('<>'))
        if parsed.scheme or parsed.netloc:
            continue
        target = (path.parent/unquote(parsed.path)).resolve() if parsed.path else path.resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            errors.append(f'{rel}: link escapes repository: {link}')
            continue
        if not target.is_file():
            errors.append(f'{rel}: missing link/image target: {link}')
        elif parsed.fragment and target.suffix=='.md' and unquote(parsed.fragment) not in headings(target.read_text()):
            errors.append(f'{rel}: broken anchor: {link}')
    for alt in re.findall(r'!\[([^\]]*)\]\(',clean):
        if not alt.strip():
            errors.append(f'{rel}: image lacks alt text')
    for tag in re.findall(r'<img\b[^>]*>',clean):
        if not re.search(r'alt="[^"]+"',tag):
            errors.append(f'{rel}: HTML image lacks alt text')
    return errors

def validate(root=ROOT):
    errors=[]
    library=json.loads((root/'catalogue/library.json').read_text())
    journey=json.loads((root/'catalogue/journey.json').read_text())
    backlog=json.loads((root/'catalogue/backlog.json').read_text())
    errors += record_errors(library) + record_errors(journey,True)
    ids=[x['id'] for x in library+journey+backlog]
    if len(ids)!=len(set(ids)):
        errors.append('Duplicate ID across catalogues')
    if [x.get('day') for x in journey] != list(range(1,101)):
        errors.append('Journey must contain ordered days 1–100')
    for x in journey:
        for target in x['related_library']:
            if target not in {i['id'] for i in library}:
                errors.append(f"{x['id']}: invalid library reference {target}")
    all_paths=[]
    for x in library+journey:
        for field in ['path','solution']:
            if x.get(field):
                path=root/x[field]
                if not path.is_file():
                    errors.append(f"{x['id']}: missing {field}")
        if not x.get('path'):
            continue
        all_paths.append(x['path'])
        text=(root/x['path']).read_text()
        if x['id'] not in text:
            errors.append(f"{x['id']}: page lacks ID")
        sections={s.lower() for s in re.findall(r'^## (.+)$',text,re.M)}
        kind=x.get('type','day')
        required=set()
        if kind in {'exercise','ai-exercise','project'}:
            required=LAB_SECTIONS.copy()
            if kind=='ai-exercise':
                required -= {'concepts'}
                required |= {'ai task and boundaries','example interaction','expected response characteristics','independent verification','potential failure modes','final engineering decision'}
        if kind=='concept':
            required={'question','task','verification','reflection'}
        if kind=='incident':
            required={'symptoms and impact','investigation tasks','progressive hints','verification','reflection'}
        if kind=='decision':
            required={'scenario','constraints','task','verification','trade-offs','reflection'}
        if kind=='day':
            required={'learning outcomes','prerequisites','environment and scope','setup','explanation','practical task','verification','cleanup','reflection','sources'}
        # Combined headings are acceptable only if they explicitly name the section.
        missing=[s for s in required if not any(s==h or s in h for h in sections)]
        if missing:
            errors.append(f"{x['id']}: missing sections {sorted(missing)}")
        if kind=='day' and not (root/f"solutions/day-{x['day']:02}.md").is_file():
            errors.append(f"{x['id']}: missing daily solution")
    if len(all_paths)!=len(set(all_paths)):
        errors.append('Canonical paths reused by multiple records')
    for path in root.rglob('*.md'):
        if '.git' not in path.parts:
            errors += markdown_errors(root,path)
    for path in (root/'assets').rglob('*.svg'):
        try:
            tree=ET.parse(path)
            for element in tree.iter():
                if element.tag.rsplit('}',1)[-1] in {'script','foreignObject'}:
                    errors.append(f'{path.name}: unsafe SVG content')
                if any(k.startswith('on') for k in element.attrib):
                    errors.append(f'{path.name}: SVG event handler')
        except ET.ParseError as exc:
            errors.append(f'{path.name}: invalid SVG: {exc}')
    return errors

def main():
    errors=validate()
    from catalogue import render
    for name,text in render().items():
        if not (ROOT/name).exists() or (ROOT/name).read_text()!=text:
            errors.append(f'{name}: stale generated navigation')
    if errors:
        print('\n'.join(errors)); sys.exit(1)
    print('PASS: metadata, IDs, sections, references, Markdown, internal links/anchors, SVG safety and generated counts.')

if __name__=='__main__':
    main()
