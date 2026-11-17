# 第二層 Shore 0 與日本替代材料

## 已知的實作

製作者確認：第二層使用原淘寶商品的 **Shore 0 號選項**，描述為 **Shore A 0**；沒有在日本購買過同等材料。原 BOM 的半透明矽膠連結為 [淘寶 item 649539121020](https://item.taobao.com/item.htm?id=649539121020)，原文字註記為 Shore 5A。

目前不能從同一商品連結證明 0 號 SKU 的型號、硬化系統、配比或光學特性，也未取得這次實作的包裝照片／datasheet。因此保留製作者敘述，不直接把原 5A 料號套用到 0 號。

## 日本採購研究結果（2026-11-18）

**尚未找到經核實、與既有淘寶材料等效的日本 Shore A 0 商品。** 以下供小樣研究，不能當作已驗證替代品或直接大量下單的指定材料。

| 候選 | 可以確認的資料 | 限制／採購入口 |
| --- | --- | --- |
| Smooth-On Ecoflex 00-30 | 原廠標示半透明、Shore **00-30**；日本代理商有產品頁 | **不是 Shore A 0 的同義詞**，透光、變形與回復特性需比較；[日本商品頁](https://sac-corp.myshopify.com/products/ecoflex-%EF%BD%B4%EF%BD%BA%EF%BE%8C%EF%BE%9A%EF%BD%AF%EF%BD%B8%EF%BD%BD-00-30-%EF%BE%84%EF%BE%97%EF%BD%B2%EF%BD%B1%EF%BE%99%EF%BD%B7%EF%BD%AF%EF%BE%84)、[原廠](https://www.smooth-on.com/products/ecoflex-00-30/) |
| Smooth-On Ecoflex 00-50 | 原廠標示半透明、Shore **00-50**；日本代理商有產品頁 | 同樣不等於 Shore A 0；日本頁另外列出約 1A，不能當作精確等效品；[日本商品頁](https://sac-corp.myshopify.com/products/ecoflex-00-50-%EF%BD%B4%EF%BD%BA%EF%BE%8C%EF%BE%9A%EF%BD%AF%EF%BD%B8%EF%BD%BD)、[原廠](https://www.smooth-on.com/products/ecoflex-00-50/) |
| 株式会社ワイテック的 Shore A 0 材料／試作服務 | [公司材料頁](https://ytc-eng.com/silicon_syurui) 明列兩種 Shore A 0 矽膠，其中一種為黏著型，色相均為乳白色 | 是日本加工商的材料／試作選項，**不是已確認可零售的 A/B 原料，也不是 Amazon 商品**。可詢問試樣、原料供應及光學規格；乳白程度是否適合本感測器仍須驗證 |
| Amazon JP 的 0A／超軟矽膠 | [Shore 0A 搜尋入口](https://www.amazon.co.jp/s?k=Shore+0A+silicone)、[SANAAA 搜尋入口](https://www.amazon.co.jp/s?k=SANAAA+%E3%82%B7%E3%83%AA%E3%82%B3%E3%83%B3+0A) | 未核實符合規格的 SKU。不能用「ぷにぷに」「gel」「soft」等商品名稱推定硬度、耐撕裂或感測用途相容性 |

查閱的 SAC 個別 Ecoflex 商品頁皆出現「売り切れ」文字；雖首頁有列價與商品入口，**不能據此認定現在有庫存**。應向供應商確認可訂購包裝、交期及規格。Amazon 商品頁在本次查核中無法完整讀取，BOM 的搜尋入口不代表有貨或相容。

若要求供應商明確標示 **Shore A 0**，可先詢問ワイテック能否供應試片或原料；目前只能確認其材料／加工服務頁面，不保證原料零售。若希望自行少量澆注，Ecoflex 00-30 有可追溯的原廠規格和日本供應管道，但它是另一個硬度量表與配方。這些是選樣路徑，不是認定與淘寶材料等效。[日本代理商系列說明](https://sac-corp.co.jp/categories/additive_silicone.php)

## 三層不可混淆

| 層 | 功能／本版狀態 |
| --- | --- |
| 第一層透明層 | 要維持透明介質功能；原 BOM 指 9345，未指定日本等效品 |
| 第二層半透明層 | 本版由原 BOM 的 Shore A 5 改為淘寶 Shore 0 號；日本替代尚待測試 |
| 第三層黑色層 | 遮光表皮；原始 9DTact 使用 Ecoflex 00-30 加黑色矽膠顏料，不代表本版第二層就是 Ecoflex 00-30 |

## 替代品小樣紀錄

1. 保留既有淘寶材料做對照；以相同模具幾何、相同厚度製作試片。
2. 按各產品原廠資料操作，記錄重量、混合方式、溫度、脫泡與硬化時間。**不跨品牌沿用混合比例，也不自行添加軟化劑作為「0A 配方」。**
3. 在正式模具材質、表面處理與接著劑上先做硬化相容性測試；原廠指出付加型矽膠可能受接觸物影響而硬化不良。[Smooth-On 原廠說明](https://www.smooth-on.com/products/ecoflex-00-30/)
4. 固定同一相機、LED、曝光和增益，比較無接觸影像、接觸對比、透光／散射、殘留形變、回復速度、黏性、撕裂與層間黏合。
5. 經機構與感測驗證後再把 BOM 狀態由 `candidate` 改成 `lab_validated`，附上製作紀錄；量測精度需重新校正與驗證。

尚未訂定接受門檻；請依實驗室用途填寫 [製作紀錄](BUILD_RECORD_TEMPLATE.md)，不要把候選材料寫成通過測試。
