# Japan BOM / 日本採購與製作表

查核日期：2026-11-18。此表由 [bom_jp.json](bom_jp.json) 產生。

**這是採購交接草稿，尚未完成日本材料的整機重製驗證。** 相機是製作者曾購買的 Amazon JP 項目；其他 Amazon「搜尋」連結不是已核實商品、庫存或相容性保證。未取得各材料耗用量與修改後五金數量，不能據此計算整機成本。

★ = 製作者指定沿用並跳過採購。`builder_purchased` = 製作者曾買過，並非本次重測。`candidate` = 有可查的候選供應來源，須實測。`search_only` = 只有搜尋／選型入口。`fabrication_required` = 須加工／列印，可能仍缺生產檔。`conditional` / `optional` = 先確認需求。

## 優先處理

- 第二層：保留淘寶 Shore 0 號為目前已知實作；日本 Shore A 0 等效品尚未核實。[材料研究與小樣方案](../docs/MATERIALS.zh-TW.md)。
- Window：透明壓克力送 Hazaiya，需補最終圖面；模具用 3D 列印，**不購買原版壓克力模具板**。
- 底座先補 STL/STEP；取得列印模具檔；相機的 USB 轉接板是否另購先核對變體。
- Ecoflex 日本個別商品頁出現「売り切れ」；頁面存在不等於有貨，交期須另確認。

## 感測器零件與材料

| ID | 項目／用途 | 數量基準 | 規格／候選 | 日本採購／檔案 | 狀態與驗證事項 |
| --- | --- | --- | --- | --- | --- |
| JP-01 | 相機 | 1／sensor | 製作者曾購買 ASIN B0C5W1QF65；不從原 BOM 推定本商品的感光元件或鏡頭規格。 | [Amazon JP 商品：B0C5W1QF65](https://www.amazon.co.jp/dp/B0C5W1QF65) | `builder_purchased`<br>製作者提供的購買連結；本次頁面無法讀取，型號、變體、FOV、PCB 厚度與介面待補。 |
| JP-02 | CSI → USB 轉接板 | 有需要才購買／sensor | 原 BOM 列獨立轉接板；本版相機是否已具 USB 請先確認。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=OV5647+CSI+USB+%E5%A4%89%E6%8F%9B+%E3%83%9C%E3%83%BC%E3%83%89) | `conditional`<br>不可把一般 CSI 排線轉接板當成 USB 視訊轉換器；USB/UVC、sensor 支援、排線腳位與尺寸須核對。 |
| JP-03 | 透明壓克力 camera window | 1／sensor，備品另計 | 原版板厚 2 mm 僅作參考；最終厚度、外形、公差待量測出圖。 | [はざいや](https://www.hazaiya.co.jp/)<br>[圖面詢價](https://www.hazaiya.co.jp/index.php/estimate-drawing)<br>[發包說明](../docs/WINDOW_OUTSOURCING.zh-TW.md) | `fabrication_required`<br>製作者指定可找此店發包；未提供已下單規格。只有 window 發包壓克力，其餘模具列印。 |
| JP-04 | 第一層透明矽膠 | 依批次量測耗用量 | 原 BOM 指透明 9345；日本同等材料未核實。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=9345+%E9%80%8F%E6%98%8E+%E3%82%B7%E3%83%AA%E3%82%B3%E3%83%BC%E3%83%B3+%E4%BB%98%E5%8A%A0%E5%9E%8B)<br>[日本代理商材料目錄](https://sac-corp.co.jp/categories/additive_silicone.php) | `search_only`<br>需確認透明度、硬化系統、硬度及層間相容性；不是任意透明型取り材皆可替代。 |
| JP-05 | 第二層半透明矽膠：Shore 0 | 依批次量測耗用量 | 已知實作：原淘寶 item 649539121020 選 Shore 0 號（製作者描述為 Shore A 0）；日本替代未驗證。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=Shore+0A+silicone+translucent)<br>[SAC Ecoflex 00-30 候選](https://sac-corp.myshopify.com/products/ecoflex-%EF%BD%B4%EF%BD%BA%EF%BE%8C%EF%BE%9A%EF%BD%AF%EF%BD%B8%EF%BD%BD-00-30-%EF%BE%84%EF%BE%97%EF%BD%B2%EF%BD%B1%EF%BE%99%EF%BD%B7%EF%BD%AF%EF%BE%84)<br>[SAC Ecoflex 00-50 候選](https://sac-corp.myshopify.com/products/ecoflex-00-50-%EF%BD%B4%EF%BD%BA%EF%BE%8C%EF%BE%9A%EF%BD%AF%EF%BD%B8%EF%BD%BD)<br>[日本 Shore A 0 試作／材料詢問](https://ytc-eng.com/silicon_syurui)<br>[材料研究](../docs/MATERIALS.zh-TW.md) | `candidate`<br>00-30／00-50 不等於 A0；日方頁面有售罄文字。先小樣比較光學、回復及黏合；不可按已驗證替代品下單。 ワイテック列有乳白色 A0 材料／試作，但原料零售與光學適用性未確認。 |
| JP-06 | 第三層黑色表皮用矽膠 | 依批次量測耗用量 | 原 9DTact 採 Ecoflex 00-30 加黑色顏料；本次實作用料包裝待補。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=Smooth-On+Ecoflex+00-30)<br>[SAC Ecoflex 00-30](https://sac-corp.myshopify.com/products/ecoflex-%EF%BD%B4%EF%BD%BA%EF%BE%8C%EF%BE%9A%EF%BD%AF%EF%BD%B8%EF%BD%BD-00-30-%EF%BE%84%EF%BE%97%EF%BD%B2%EF%BD%B1%EF%BE%99%EF%BD%B7%EF%BD%AF%EF%BE%84)<br>[原廠規格](https://www.smooth-on.com/products/ecoflex-00-30/) | `candidate`<br>日本代理商有頁面，但頁面出現售罄，庫存須確認。第三層配方不可誤當第二層已驗證配方。 |
| JP-07 | 黑色矽膠顏料 | 批次耗材 | 候選：Smooth-On Silc Pig 黑色；須確認黑色包裝而非僅顏色樣本。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=Smooth-On+Silc+Pig+black)<br>[SAC Silc-PIG](https://sac-corp.myshopify.com/products/silc-pig-9%E3%82%AB%E3%83%A9%E3%83%BC%E3%82%B5%E3%83%B3%E3%83%97%E3%83%A9%E3%83%BC)<br>[原廠相容性](https://www.smooth-on.com/products/silc-pig/) | `candidate`<br>顏料含量、遮光與硬化須試驗；不可直接以一般樹脂顏料／墨水替代。 |
| JP-08 | M2 熱熔嵌件 | 原版參考 8；修改版待核對 | 原 BOM 標為 M2-5-3；長度／外徑的標示順序未核實。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=M2+%E3%82%A4%E3%83%B3%E3%82%B5%E3%83%BC%E3%83%88%E3%83%8A%E3%83%83%E3%83%88+%E7%9C%9F%E9%8D%AE+5+3) | `search_only`<br>先依原商品圖及 CAD 確認螺紋、body length、OD、孔徑與埋深，再選 SKU；嵌件不一定是 3.2mm 外徑通用品。 |
| JP-09 | 底座／外殼 M2 螺絲 | 原版參考 4；修改版待核對 | 原 BOM M2 × 6 mm；頭型、材質與有效牙長需配合實物。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=M2+6mm+%E5%B0%8F%E3%81%AD%E3%81%98+%E3%82%B9%E3%83%86%E3%83%B3%E3%83%AC%E3%82%B9) | `search_only`<br>購買機械牙，不是自攻螺絲；檢查頭高、PCB 間隙與是否頂底。 |
| JP-10 | 模具 M3 螺帽 | 原版參考 8／套；列印模具待核對 | M3；依實際 3D 列印模具的夾持設計確認是否沿用。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=M3+%E5%85%AD%E8%A7%92%E3%83%8A%E3%83%83%E3%83%88+%E3%82%B9%E3%83%86%E3%83%B3%E3%83%AC%E3%82%B9) | `search_only`<br>不可把原壓克力模具用量直接視為列印模具用量。 |
| JP-11 | 模具 M3 螺絲 | 原版參考 8／套；列印模具待核對 | 原 BOM M3 × 30 mm；依列印模具堆疊厚度與夾持方式確認。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=M3+30mm+%E5%B0%8F%E3%81%AD%E3%81%98+%E3%83%8A%E3%83%83%E3%83%88) | `search_only`<br>先核對夾緊長度與孔位；不是已驗證列印模具五金。 |

## ★ 沿用，跳過採購

| ID | 項目／用途 | 數量基準 | 規格／候選 | 日本採購／檔案 | 狀態與驗證事項 |
| --- | --- | --- | --- | --- | --- |
| JP-24 | ★ LED 板／既有線路 | 1／sensor，來自既有零件 | Reuse existing LED assembly. 日本發包暫跳過。 | 待補 | `reuse_skip`<br>不提供一般 LED 環作等效替代；接手需記錄既有零件 ID、接線、方向與供電。 |
| JP-25 | ★ 白色 sensor shell | 1／sensor，來自既有零件 | Reuse existing white shell. **不能用 PLA 列印。** 日本發包暫跳過。 | 待補 | `reuse_skip`<br>材質／製程涉及光學透光與散射；本次未驗證替代品。 |

## 自行製作／加工件

| ID | 項目／用途 | 數量基準 | 規格／候選 | 日本採購／檔案 | 狀態與驗證事項 |
| --- | --- | --- | --- | --- | --- |
| JP-26 | 修改版底座 | 1／sensor | sensor_base_adapt_for_thick_PCB.SLDPRT | [SolidWorks source](../hardware/cad/sensor_base_adapt_for_thick_PCB.SLDPRT) | `fabrication_required`<br>尚缺 STL/STEP；列印材料、切片參數與 PCB 配合尺寸待補。 |
| JP-27 | 修改版 camera isolation ring | 1／sensor | isolation_ring_out_11.4_in_10.3.STL | [STL](../hardware/mesh/isolation_ring_out_11.4_in_10.3.STL) | `fabrication_required`<br>檔名不是尺寸驗證；確認 mm 比例、列印設定與實物遮光效果。 |
| JP-28 | LEAP fingertip 固定件 | 依裝設手指數量 | STL chip-holder 版及 SolidWorks 版均保留，不假設兩檔同版。 | [STL](../hardware/mesh/finger_tip_tactile_with_chip_holder.STL)<br>[SolidWorks](../hardware/cad/finger_tip_tactile1_wrq.SLDPRT) | `fabrication_required`<br>由 LEAP 官方 CAD 修改；原授權條款待核對。固定螺絲、材質及手部行程待量測。 |
| JP-29 | 3D 列印 casting molds | 1 套／製作工位 | 使用 3D 列印模具，取消原版壓克力 mold 板採購。 | [製作缺口](../docs/KNOWN_GAPS.md) | `fabrication_required`<br>本版列印檔尚未提供；原上游 DXF 僅幾何參考，需建成實體並確認厚度、密封與脫模。 |
| JP-30 | Calibration board | 校正時使用／共用 | 使用上游 calibration_board 檔案。 | [上游 fabrication](https://github.com/linchangyi1/9DTact/tree/main/9DTact_Design/fabrication) | `conditional`<br>此 repo 未複製上游檔；新材料或機構變動後應重新校正。 |

## 共用工具、耗材與選配

| ID | 項目／用途 | 數量基準 | 規格／候選 | 日本採購／檔案 | 狀態與驗證事項 |
| --- | --- | --- | --- | --- | --- |
| JP-12 | 電子秤 | 實驗室共用 1 台 | 依最小 A/B 加料量與顏料量選解析度；0.01g 等級可作選型起點，須確認量程與校驗。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB%E3%82%B9%E3%82%B1%E3%83%BC%E3%83%AB+0.01g+%E6%A0%A1%E6%AD%A3) | `search_only`<br>顯示解析度不等於量測精度；尚未指定 SKU。 |
| JP-13 | 熱熔膠槍 | 有需求才使用／共用 | 接線或非光學處暫固定工具；不是 window 或矽膠的指定接著劑。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=goot+%E3%82%B0%E3%83%AB%E3%83%BC%E3%82%AC%E3%83%B3+AC100V) | `search_only`<br>依實際固定位置、耐熱與拆修需求確認是否需要；不把熱熔膠放進光路。 |
| JP-14 | 溫控烙鐵／工具 | 實驗室共用 | 候選：HAKKO FX600-02（日本 100V）；嵌件工具頭與焊接工具需依用途分開選。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=HAKKO+FX600-02)<br>[HAKKO 原廠](https://www.hakko.com/japan/products/hakko_fx600.html) | `candidate`<br>本次未核實 Amazon SKU／庫存；LED 沿用，是否需焊接由現有線路狀態決定。 |
| JP-15 | 刀具 | 實驗室共用 | 精密修邊刀具；依實際需要與刀刃形式選購。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=%E7%B2%BE%E5%AF%86+%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%83%8A%E3%82%A4%E3%83%95) | `search_only`<br>用途為修邊；避免傷害接觸表皮與 window；SKU 未核實。 |
| JP-16 | 混合杯 | 每批耗材 | PP 等可相容的乾淨容器，容量需預留脫泡膨脹空間。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=PP+%E8%A8%88%E9%87%8F%E3%82%AB%E3%83%83%E3%83%97+%E4%BD%BF%E3%81%84%E6%8D%A8%E3%81%A6+%E6%A8%B9%E8%84%82) | `search_only`<br>材質與矽膠的硬化相容性先小樣確認。 |
| JP-17 | 攪拌棒 | 每批耗材 | 乾淨塑膠攪拌棒，避免未驗證表面處理物污染。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=%E3%83%97%E3%83%A9%E3%82%B9%E3%83%81%E3%83%83%E3%82%AF+%E6%94%AA%E6%8B%8C%E6%A3%92+%E3%82%B7%E3%83%AA%E3%82%B3%E3%83%B3) | `search_only`<br>依原廠指示充分混合；每種材料工具保持分開。 |
| JP-18 | 除塵／低掉屑清潔耗材 | 批次耗材 | 原 BOM 為 Dust removal paper；低掉屑拭紙、除塵貼等功能不同，要依使用位置選。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=%E3%83%AC%E3%83%B3%E3%82%BA+%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%E3%83%9A%E3%83%BC%E3%83%91%E3%83%BC+%E3%83%80%E3%82%B9%E3%83%88%E9%99%A4%E5%8E%BB+%E3%82%B7%E3%83%BC%E3%83%AB) | `search_only`<br>確認不留膠、不刮傷、不帶入硬化抑制物；不把帶膠除塵貼當光學擦拭紙。 |
| JP-19 | 塑膠針筒 | 每批耗材 | 無針、容量依實際注入量；需確認密封件與矽膠相容性。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=%E6%A8%B9%E8%84%82+%E6%B3%A8%E5%85%A5+%E3%82%B7%E3%83%AA%E3%83%B3%E3%82%B8+%E9%87%9D%E3%81%AA%E3%81%97) | `search_only`<br>只作施膠／注料用途；確認實際接液材料。 |
| JP-20 | Window 接著劑 | 批次耗材 | 透明、適用 PMMA 與現有白色外殼，需密封；原 BOM 未給出可辨識的日方等效型號。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=%E3%82%A2%E3%82%AF%E3%83%AA%E3%83%AB+%E3%83%8A%E3%82%A4%E3%83%AD%E3%83%B3+%E6%8E%A5%E7%9D%80%E5%89%A4+%E9%80%8F%E6%98%8E) | `search_only`<br>暫不指定通用強力膠；先測 PMMA 霧化、龜裂、黏合、對矽膠硬化及光路的影響。 |
| JP-21 | 黑色層黏合／修補膠 | 有需要才使用 | 候選：Smooth-On Sil-Poxy，限實際需要矽膠接著或修補的位置。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=Smooth-On+Sil-Poxy)<br>[SAC Sil-Poxy](https://sac-corp.myshopify.com/products/sil-poxy)<br>[日本代理商技術資料](https://sac-corp.co.jp/products/Sil-Poxy_TI.pdf) | `candidate`<br>不是原黑色層整面塗膠的已驗證配方；避免用較硬膠層改變接觸層力學。 |
| JP-22 | 真空脫泡設備 | 實驗室共用 | 真空泵＋耐真空腔體＋接頭；日本 100V、容積、壓力與混合料膨脹餘量需選型。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=%E7%9C%9F%E7%A9%BA+%E8%84%B1%E6%B3%A1+%E3%83%81%E3%83%A3%E3%83%B3%E3%83%90%E3%83%BC+%E3%83%9D%E3%83%B3%E3%83%97+100V+%E3%82%B7%E3%83%AA%E3%82%B3%E3%83%B3) | `search_only`<br>原 28×28cm+8L／6L+4L 為淘寶選項文字，不是必須照買；未核實日本套裝與接頭相容性。 |
| JP-23 | 固化加熱設備 | 選配／共用 | 僅在選用材料允許的硬化／後固化條件下使用；本版實作溫度與時間尚未記錄。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=%E6%81%92%E6%B8%A9%E5%99%A8+%E4%B9%BE%E7%87%A5%E5%99%A8+%E5%AE%9F%E9%A8%93%E7%94%A8+%E4%BD%8E%E6%B8%A9) | `optional`<br>不沿用不同材料的加熱配方；原 BOM 亦列為 optional。 |
| JP-31 | 線材固定與拉力釋放 | 依 LEAP 布線 | 小型束帶／適當線材固定件；不是原 BOM 指定品。 | [Amazon JP 搜尋（未核實 SKU）](https://www.amazon.co.jp/s?k=%E7%B5%90%E6%9D%9F%E3%83%90%E3%83%B3%E3%83%89+%E5%B0%8F%E5%9E%8B+%E3%82%B1%E3%83%BC%E3%83%96%E3%83%AB+%E5%9B%BA%E5%AE%9A) | `optional`<br>依實際線徑與關節活動量確認，不夾壓 FPC 或限制關節。 |

## 使用與維護

原始淘寶對照見 [TAOBAO_REFERENCE.md](TAOBAO_REFERENCE.md)。原版五金數量只作參考，LEAP 固定件與修改後底座應重新核對。`M2-5-3` 的順序須依原商品尺寸圖解讀，不直接推定長度或外徑。

將項目改為 `lab_validated` 時，請填入確切商品／變體、購買日期、加工或材料參數，並附 [製作紀錄](../docs/BUILD_RECORD_TEMPLATE.md)。更換相機、矽膠或光學件後，應重新校正並驗證感測表現。

採購價格、出貨地、庫存及運費未核實；此表不含虛構的日本購入實績。
