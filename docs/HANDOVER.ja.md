# 製作・引き継ぎガイド

[English](HANDOVER.md) · **日本語** · [部品表](../bom/BOM_JP.md) · [材料ガイド](MATERIALS.ja.md)

[9DTact](https://github.com/linchangyi1/9DTact) の厚いカメラ基板への対応と LEAP Hand への取り付けを変更しています。校正、形状復元、力推定には元のソフトウェアを使用します。

## まず元の製作動画を見る

[![▶ 9DTact Fabrication Tutorial](https://i.ytimg.com/vi/VxMceWVz7QQ/hqdefault.jpg)](https://www.youtube.com/watch?v=VxMceWVz7QQ)

[▶ 9DTact Fabrication Tutorial](https://www.youtube.com/watch?v=VxMceWVz7QQ) を見てから、以下の構成と組み立て手順に沿って Hashimoto Lab 版を製作します。

## 構成

| 項目 | Hashimoto Lab の実装 |
| --- | --- |
| 第1層 | 透明 9345 シリコーン。恵州ラベルとQRコードのある白い容器 |
| 第2層 | Taobao の **Shore A 0**。元の 5A から変更。「0」ラベルの容器 |
| 第3層 | 黄色・青色容器の [シリコーン](https://amzn.asia/d/08yFspH2) ＋ [黒色顔料](https://ja.aliexpress.com/item/1005012698616201.html) |
| センサベース | [厚い基板用ベース、STL・SolidWorks](../hardware/README.md) |
| 遮光リング | [変更版リング、STL・SolidWorks](../hardware/README.md) |
| LEAP 取り付け部品 | [チップホルダー付き STL と SolidWorks の別バリエーション](../hardware/README.md)。公式 LEAP CAD から改変 |
| カメラ | [Amazon Japan B0C5W1QF65](https://www.amazon.co.jp/dp/B0C5W1QF65) |
| アクリル窓 | [はざいやに外注](WINDOW_OUTSOURCING.md) |
| 注型モールド | **3D プリント** |
| ★ CSI–USB 基板・LED 基板・白色シェル | **既存品を再利用。白色シェルは PLA で造形しない。** |

材料と LED 基板の実物写真は [部品表](../bom/BOM_JP.md) にあります。

## 製作前の準備

1. 再利用する部品、ケーブル、ねじをそろえます。
2. [STL](../hardware/README.md) を取得し、mm 単位のスケールとカメラ基板の仮組みを確認します。
3. モールドデータを取得し、[窓の加工図面](WINDOW_OUTSOURCING.md) を準備します。
4. [部品表](../bom/BOM_JP.md) の材料と工具を用意します。

## 組み立て

1. **機構を仮組みする。** 基板の収まり、レンズの隙間、LED、遮光リング、シェル、ねじの締結状態を確認します。
2. **カメラと照明を確認する。** 既存の CSI–USB 基板と LED を接続し、露光、ゲイン、焦点を設定します。配線を挟まないように通します。
3. **アクリル窓を取り付ける。** 光学面を清掃し、密封、接着、曇りを確認します。
4. **第1層を注型する。** 透明シリコーンを使用します。
5. **第2層を注型・脱型する。** Shore A 0 を使用します。**指で端を押したり引いたりせず、カッターナイフでモールドとシリコーンの界面を分離します。** [比較図と手順](DEMOLDING.md)。
6. **第3層を注型・脱型する。** 指定シリコーンに黒色顔料を加え、接触面と必要な側面を遮光します。同じナイフによる脱型方法を使い、**感圧面と黒色表皮を切らないようにします**。
7. **LEAP Hand に取り付ける。** ねじ、関節可動域、干渉、ケーブルの余裕を確認します。
8. **基準画像を取得して再校正する。** [元の校正手順](https://github.com/linchangyi1/9DTact#3d-shape-reconstruction) に従い、変更後の力推定精度も評価します。

配合、脱泡、硬化、造形条件は [製作記録](BUILD_RECORD_TEMPLATE.md) に残します。

## 最終確認

| 確認内容 | 製作記録に残す情報 |
| --- | --- |
| 安定した非接触画像 | 元画像、露光、ゲイン |
| 中央と周辺の接触応答 | 試験画像と試験物 |
| 繰り返し接触後の回復・表皮の状態 | 回数、回復時間、写真 |
| LEAP 動作中の干渉・配線の引張り | 取り付け写真、動作動画 |
| 校正と力推定 | ソフトウェアの版、データ、実測誤差 |

[追加するデータ・条件の一覧 →](KNOWN_GAPS.md)
