#!/usr/bin/env python3
"""Render the Japanese procurement table from its JSON source (stdlib only)."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', '<br>')


def render(data):
    lines = [
        '# Japan BOM / 日本採購與製作表', '',
        f'查核日期：{data["review_date"]}。此表由 [bom_jp.json](bom_jp.json) 產生。', '',
        '**這是採購交接草稿，尚未完成日本材料的整機重製驗證。** 相機是製作者曾購買的 Amazon JP 項目；其他 Amazon「搜尋」連結不是已核實商品、庫存或相容性保證。未取得各材料耗用量與修改後五金數量，不能據此計算整機成本。', '',
        '★ = 製作者指定沿用並跳過採購。`builder_purchased` = 製作者曾買過，並非本次重測。`candidate` = 有可查的候選供應來源，須實測。`search_only` = 只有搜尋／選型入口。`fabrication_required` = 須加工／列印，可能仍缺生產檔。`conditional` / `optional` = 先確認需求。', '',
        '## 優先處理', '',
        '- 第二層：保留淘寶 Shore 0 號為目前已知實作；日本 Shore A 0 等效品尚未核實。[材料研究與小樣方案](../docs/MATERIALS.zh-TW.md)。',
        '- Window：透明壓克力送 Hazaiya，需補最終圖面；模具用 3D 列印，**不購買原版壓克力模具板**。',
        '- 底座先補 STL/STEP；取得列印模具檔；相機的 USB 轉接板是否另購先核對變體。',
        '- Ecoflex 日本個別商品頁出現「売り切れ」；頁面存在不等於有貨，交期須另確認。', '',
    ]
    for section in data['sections']:
        lines += [f'## {section["title"]}', '',
                  '| ID | 項目／用途 | 數量基準 | 規格／候選 | 日本採購／檔案 | 狀態與驗證事項 |',
                  '| --- | --- | --- | --- | --- | --- |']
        for item in data['items']:
            if item['section'] != section['id']:
                continue
            links = '<br>'.join(f'[{cell(link["label"])}]({link["url"]})' for link in item['links']) or '待補'
            row = [item['id'], item['name'], item['quantity_basis'], item['specification'], links,
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / 'bom/bom_jp.json').read_text())
    content = render(data)
    target = ROOT / 'bom/BOM_JP.md'
    if args.check:
        if not target.exists() or target.read_text() != content:
            raise SystemExit('BOM_JP.md is stale; run python3 scripts/render_bom.py')
        print(f'BOM table matches JSON: {len(data["items"])} entries')
    else:
        target.write_text(content)
        print(f'Wrote {target.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
