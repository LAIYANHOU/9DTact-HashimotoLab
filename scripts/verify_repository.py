#!/usr/bin/env python3
"""Check supplied file hashes, STL structure and local Markdown links.

This is a documentation/inventory check, not a physical validation.
"""
import hashlib
import json
import math
import re
import struct
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def verify():
    errors = []
    manifest = json.loads((ROOT / 'hardware/manifest.json').read_text())
    for item in manifest['files']:
        path = ROOT / item['path']
        if not path.is_file():
            errors.append(f'Missing file: {item["path"]}')
            continue
        raw = path.read_bytes()
        if len(raw) != item['bytes'] or hashlib.sha256(raw).hexdigest() != item['sha256']:
            errors.append(f'Checksum/size mismatch: {item["path"]}')
        if path.suffix.lower() == '.stl':
            if len(raw) < 84:
                errors.append(f'STL too short: {item["path"]}')
                continue
            count = struct.unpack_from('<I', raw, 80)[0]
            if len(raw) != 84 + 50 * count:
                errors.append(f'Invalid binary STL size: {item["path"]}')
                continue
            vertices = [struct.unpack_from('<3f', raw, 84 + 50*i + 12 + 12*j)
                        for i in range(count) for j in range(3)]
            if not vertices or not all(math.isfinite(v) for point in vertices for v in point):
                errors.append(f'Invalid vertices: {item["path"]}')
            else:
                extents = [max(p[k] for p in vertices)-min(p[k] for p in vertices) for k in range(3)]
                expected = item['mesh']['coordinate_extents']
                if count != item['mesh']['triangles'] or any(abs(a-b) > 1e-5 for a, b in zip(extents, expected)):
                    errors.append(f'Mesh inventory mismatch: {item["path"]}')
    pattern = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
    for path in ROOT.rglob('*.md'):
        if '.git' in path.relative_to(ROOT).parts:
            continue
        for target in pattern.findall(path.read_text()):
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            local = unquote(target.split('#')[0])
            if not (path.parent / local).exists():
                errors.append(f'Broken local link: {path.relative_to(ROOT)} -> {target}')
    data = json.loads((ROOT / 'bom/bom_jp.json').read_text())
    ids = [item['id'] for item in data['items']]
    if len(set(ids)) != len(ids):
        errors.append('Duplicate BOM IDs')
    for item in data['items']:
        for link in item['links']:
            url = urlsplit(link['url'])
            if url.hostname == 'www.amazon.co.jp' and url.path == '/s' and link['kind'] != 'search':
                errors.append(f'{item["id"]}: Amazon search link mislabeled')
        if item['status'] == 'lab_validated' and not item.get('build_record'):
            errors.append(f'{item["id"]}: physical validation needs a build record')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(manifest["files"])} supplied hardware files, STL structure, local links and {len(ids)} BOM IDs')
    print('Not checked: physical fit, CAD configurations, material performance, live stock or external links')


if __name__ == '__main__':
    verify()
