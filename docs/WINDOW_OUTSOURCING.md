# Acrylic camera window / アクリル窓の外注

[Handover](HANDOVER.md) · [引き継ぎガイド](HANDOVER.ja.md)

The builder recommends **[Hazaiya / はざいや](https://www.hazaiya.co.jp/)** for the clear acrylic optical window. Only the window is outsourced in acrylic; **casting molds are 3D printed**.

製作者は透明アクリルの光学窓の外注先として「はざいや」を指定しています。注型用モールドは 3D プリントするため、元のアクリル製モールド板を一緒に発注しないでください。

## Drawing checklist / 図面の確認

| Field / 項目 | Required information / 確認内容 |
| --- | --- |
| Material / 材料 | Clear PMMA; grade and manufacturing type to be selected / 透明 PMMA、グレードと製法を確認 |
| Thickness / 板厚 | Original design's 2 mm is only a reference; measure this build / 元の 2 mm は参考値。実物に合わせて確定 |
| Outline and mating surfaces / 外形・取付面 | Confirm against the existing white shell and window / 既存の白色シェルと窓に合わせて確認 |
| Dimensions and tolerances / 寸法・公差 | Define fit, critical dimensions and machining requirements / はめ合い、重要寸法、加工方法を指定 |
| Optical surfaces / 光学面 | Protect the clear faces; establish scratch/fogging acceptance limits / 傷・白濁の許容基準を確認 |
| Quantity / 数量 | One per sensor, plus lab-selected spares / センサ1個につき1枚、予備数は別途決定 |
| Final files / 最終データ | Window-specific DXF, SVG or AI plus a dimensioned reference drawing / 窓専用の加工データと寸法図を準備 |

Upstream `mold_*.DXF` files are mold geometry, not automatically the window production drawing. Confirm the existing window or suitable assembly CAD before exporting the final outline.

元の `mold_*.DXF` はモールド用の形状です。窓の加工図としてそのまま使わず、実物または組立 CAD を確認してください。[元の fabrication データ](https://github.com/linchangyi1/9DTact/tree/main/9DTact_Design/fabrication)。

## Quotation / 見積もり

Hazaiya's [drawing quotation page](https://www.hazaiya.co.jp/index.php/estimate-drawing) lists DXF, AI and SVG uploads. Use the [machining order information](https://www.hazaiya.co.jp/estimate) to discuss a process appropriate to the required tolerances.

Fill every bracketed field before sending this Japanese inquiry:

> 視覚式触覚センサのカメラ窓として使用する、透明アクリル部品の見積りをお願いします。添付図面の寸法単位は mm です。板厚［確定値］、数量［数量］、重要寸法・公差［図面参照］です。カメラの光路に入るため、両面の傷・白濁を避けたいです。希望公差に適した加工方法、材料、納期、価格をご提案ください。保護フィルムの有無もご教示ください。

Check the received part by dry-fitting and inspecting the optical path. Archive the final drawing, quotation specifications and measurements in the build record.

受領後は仮組みと光学面を確認し、最終図面、見積もり仕様、実測値を製作記録に保存してください。
