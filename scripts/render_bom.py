#!/usr/bin/env python3
"""Render the Japanese procurement table from its JSON source (stdlib only)."""
import argparse
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', '<br>')


def photo_cell(item):
    photo = item.get('photo')
    if not photo:
        return ''
    path = escape(photo['path'], quote=True)
    alt = escape(photo['alt_en'], quote=True)
    return f'<a href="{path}"><img src="{path}" width="90" alt="{alt}"></a>'


def status_label(item, language):
    labels = {
        'builder_purchased': ('Purchased', '曾購買'),
        'builder_specified': ('Selected', '指定品'),
        'builder_confirmed': ('Confirmed', '已確認'),
        'candidate': ('Candidate', '候選'),
        'search_only': ('Search', '搜尋'),
        'fabrication_required': ('Fabricate', '製作'),
        'conditional': ('If needed', '視需求'),
        'optional': ('Optional', '選用'),
        'reuse_skip': ('Reuse', '沿用'),
        'lab_validated': ('Lab tested', '實測'),
    }
    label = labels[item['status']][0 if language == 'en' else 1]
    return f'**{label}**'


def render_zh(data):
    lines = [
        '# 日本採購與製作表', '',
        '[English BOM](BOM_JP.md) · **繁體中文**', '',
        'Hashimoto Lab 的零件、材料與共用工具。★ 代表沿用實驗室既有零件。', '',
        '[材料指南 · English](../docs/MATERIALS.md) · [材料 · 日本語](../docs/MATERIALS.ja.md)', '',
    ]
    for section in data['sections']:
        lines += [f'## {section["title"]}', '',
                  '| ID | 項目／用途 | Photo / 写真 | 數量 | 規格 | 採購／檔案 | 備註 |',
                  '| --- | --- | --- | --- | --- | --- | --- |']
        for item in data['items']:
            if item['section'] != section['id']:
                continue
            links = '<br>'.join(f'[{cell(link["label"])}]({link["url"]})' for link in item['links']) or '待補'
            row = [item['id'], item['name'], photo_cell(item), item['quantity_basis'], item['specification'], links,
                   f'{status_label(item, "zh")}<br>{item["validation_note"]}']
            lines.append('| ' + ' | '.join(cell(v) for v in row) + ' |')
        lines.append('')
    lines += [
        '[製作紀錄](../docs/BUILD_RECORD_TEMPLATE.md) · [原始淘寶對照](TAOBAO_REFERENCE.md) · [編輯資料來源](bom_jp.json)', '',
    ]
    return '\n'.join(lines)


def render_en(data):
    lines = [
        '# Japan BOM and fabrication list', '',
        '[Build guide](../docs/HANDOVER.md)', '',
        'Parts, materials and shared tools for the Hashimoto Lab build. **★ Reuse existing lab parts.**', '',
    ]
    for section in data['sections']:
        lines += [f'## {section["title_en"]}', '',
                  '| ID / item | Photo / 写真 | Quantity | Specification | Source / file | Notes |',
                  '| --- | --- | --- | --- | --- | --- |']
        for item in data['items']:
            if item['section'] != section['id']:
                continue
            links = '<br>'.join(f'[{cell(link["label_en"])}]({link["url"]})' for link in item['links']) or 'Reuse existing assembly'
            row = [f'**{item["id"]}**<br>{item["name_en"]}', photo_cell(item), item['quantity_basis_en'],
                   item['specification_en'], links,
                   f'{status_label(item, "en")}<br>{item["validation_note_en"]}']
            lines.append('| ' + ' | '.join(cell(value) for value in row) + ' |')
        lines.append('')
    lines += ['[Build record](../docs/BUILD_RECORD_TEMPLATE.md) · [Original Taobao references](TAOBAO_REFERENCE.md) · [Edit source data](bom_jp.json)', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / 'bom/bom_jp.json').read_text())
    for name, renderer in [('BOM_JP.md', render_en), ('BOM_JP.zh-TW.md', render_zh)]:
        content = renderer(data)
        target = ROOT / 'bom' / name
        if args.check:
            if not target.exists() or target.read_text() != content:
                raise SystemExit(f'{name} is stale; run python3 scripts/render_bom.py')
            print(f'{name} matches JSON: {len(data["items"])} entries')
        else:
            target.write_text(content)
            print(f'Wrote {target.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
