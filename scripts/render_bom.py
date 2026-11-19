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
        return '—'
    path = escape(photo['path'], quote=True)
    alt = escape(photo['alt_en'], quote=True)
    return (f'<a href="{path}"><img src="{path}" width="90" alt="{alt}"></a>'
            f'<br>{escape(photo["caption_en"])}<br>{escape(photo["caption_ja"])}')


def render_zh(data):
    lines = [
        '# 日本採購與製作表', '',
        '[English BOM](BOM_JP.md) · **繁體中文**', '',
        f'查核日期：{data["review_date"]}。此表由 [bom_jp.json](bom_jp.json) 產生。', '',
        '**這是採購交接草稿，尚未完成日本材料的整機重製驗證。** 相機是製作者曾購買的 Amazon JP 項目；第三層矽膠和顏料使用製作者指定連結，Shared tools 已由製作者確認。搜尋入口與具體商品連結分別標示。未取得各材料耗用量與修改後五金數量，不能據此計算整機成本。', '',
        '★ = 製作者指定沿用並跳過採購。`builder_purchased` = 製作者曾買過，並非本次重測。`builder_specified` = 製作者指定產品。`builder_confirmed` = 製作者已確認工具。`candidate` = 有可查的候選供應來源，須實測。`search_only` = 只有搜尋／選型入口。`fabrication_required` = 須加工／列印，可能仍缺生產檔。`conditional` / `optional` = 先確認需求。', '',
        '## 優先處理', '',
        '- 第二層：保留淘寶 Shore 0 號為目前已知實作；日本 Shore A 0 等效品尚未核實。[材料研究與小樣方案](../docs/MATERIALS.md)。',
        '- Window：透明壓克力送 Hazaiya，需補最終圖面；模具用 3D 列印，**不購買原版壓克力模具板**。',
        '- 底座 STL 已補齊；取得列印模具檔與 window 圖面；沿用現有 CSI–USB、LED 與白色外殼；不另購 CSI–USB。',
        '- 第二層候選 Ecoflex 的先前日本商品頁出現「売り切れ」；第三層則使用製作者指定的 Amazon 連結。', '',
    ]
    for section in data['sections']:
        lines += [f'## {section["title"]}', '',
                  '| ID | 項目／用途 | Photo / 写真 | 數量基準 | 規格／候選 | 日本採購／檔案 | 狀態與驗證事項 |',
                  '| --- | --- | --- | --- | --- | --- | --- |']
        for item in data['items']:
            if item['section'] != section['id']:
                continue
            links = '<br>'.join(f'[{cell(link["label"])}]({link["url"]})' for link in item['links']) or '待補'
            row = [item['id'], item['name'], photo_cell(item), item['quantity_basis'], item['specification'], links,
                   f'`{item["status"]}`<br>{item["validation_note"]}']
            lines.append('| ' + ' | '.join(cell(v) for v in row) + ' |')
        lines.append('')
    lines += [
        '## 使用與維護', '',
        '原始淘寶對照見 [TAOBAO_REFERENCE.md](TAOBAO_REFERENCE.md)。原版五金數量只作參考，LEAP 固定件與修改後底座應重新核對。`M2-5-3` 的順序須依原商品尺寸圖解讀，不直接推定長度或外徑。', '',
        '將項目改為 `lab_validated` 時，請填入確切商品／變體、購買日期、加工或材料參數，並附 [製作紀錄](../docs/BUILD_RECORD_TEMPLATE.md)。更換相機、矽膠或光學件後，應重新校正並驗證感測表現。', '',
        '採購價格、出貨地、庫存及運費未核實；此表不含虛構的日本購入實績。', '',
    ]
    return '\n'.join(lines)


def render_en(data):
    lines = [
        '# Japan BOM and fabrication list', '',
        '**English** · [繁體中文](BOM_JP.zh-TW.md)', '',
        f'Last reviewed: {data["review_date"]}. Generated from [bom_jp.json](bom_jp.json).', '',
        'This handover lists Japan sourcing routes and fabrication requirements. The camera is a builder-reported Amazon Japan purchase. Layer-3 silicone/pigment use builder-specified product links, and shared tools were reviewed by the builder on 2026-11-19. Search links are marked as sourcing routes. Material consumption and modified-build fastener quantities are not yet recorded; no total build cost is claimed.', '',
        '## Read the status before buying', '',
        '| Status | Meaning |',
        '| --- | --- |',
        '| `builder_purchased` | Builder previously purchased the linked product; not re-tested in this review |',
        '| `builder_specified` | Product link specified by the builder |',
        '| `builder_confirmed` | Shared tool reviewed and confirmed by the builder |',
        '| `candidate` | Identified candidate / supplier; physical compatibility still needs validation |',
        '| `search_only` | Search and selection route; check the item specification when ordering |',
        '| `fabrication_required` | Print or machine the part; check file and setting readiness |',
        '| `conditional` / `optional` | Confirm whether it is needed before purchasing |',
        '| `reuse_skip` · ★ | Reuse the existing lab assembly; procurement is intentionally deferred |', '',
        '## First decisions', '',
        '- **Layer 2:** keep the Taobao Shore 0 option as the recorded build material. A Japan-sourced Shore A 0 equivalent is not qualified. [English material notes](../docs/MATERIALS.md) / [日本語](../docs/MATERIALS.ja.md).',
        '- **Window:** outsource the clear acrylic optical window to Hazaiya after checking the drawing. **3D print the casting molds; do not order the original acrylic mold plates.**',
        '- **Layer 3:** use the builder-specified [silicone](https://amzn.asia/d/08yFspH2) and [black pigment](https://ja.aliexpress.com/item/1005012698616201.html).',
        '- **Reusable parts:** keep the existing ★ CSI–USB converter, ★ LED board and ★ white shell. A matching CSI–USB replacement has not been found. **Do not print the white shell in PLA.**',
        '- **Layer-2 alternatives:** earlier SAC Ecoflex pages displayed sold-out text. Confirm stock when considering those alternatives; layer 3 uses the builder-specified Amazon link.', '',
        '**Photo / 写真:** builder-supplied lab photos identify the three silicone pairs and reused LED board. Click a thumbnail for the original photo. 小画像をクリックすると元の写真を表示します。', '',
    ]
    for section in data['sections']:
        lines += [f'## {section["title_en"]}', '',
                  '| ID / item | Photo / 写真 | Quantity basis | Specification / candidate | Japan source / file | Status and checks |',
                  '| --- | --- | --- | --- | --- | --- |']
        for item in data['items']:
            if item['section'] != section['id']:
                continue
            links = '<br>'.join(f'[{cell(link["label_en"])}]({link["url"]})' for link in item['links']) or 'Reuse existing assembly'
            row = [f'**{item["id"]}**<br>{item["name_en"]}', photo_cell(item), item['quantity_basis_en'],
                   item['specification_en'], links,
                   f'`{item["status"]}`<br>{item["validation_note_en"]}']
            lines.append('| ' + ' | '.join(cell(value) for value in row) + ' |')
        lines.append('')
    lines += ['## Keep the next build reproducible', '',
              'Legacy purchasing references: [TAOBAO_REFERENCE.md](TAOBAO_REFERENCE.md). Original-design fastener counts are references, not measurements of the modified assembly. Resolve the legacy `M2-5-3` dimensional order against its drawing before selecting inserts.', '',
              'To mark an item `lab_validated`, add its exact product/variant, date, material or fabrication settings and a completed [build record](../docs/BUILD_RECORD_TEMPLATE.md). Recalibrate after changing the camera, optical parts, silicone or mechanics; separately validate any learned force model.', '',
              'Prices, shipping origin, stock and shipping cost are not verified. Japanese lab purchase history has not been invented for any candidate.', '']
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
