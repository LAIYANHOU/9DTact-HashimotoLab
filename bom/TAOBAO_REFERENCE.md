# Original Taobao BOM cross-reference

Source: builder-supplied `9DTact_BOM.docx`, SHA-256 `d317036f378e364810e694dd7d54bc09adf9a878556ee6e7c6a72537ca8c008c`. The original remains in the parent handover folder and is not redistributed here.

Original purchasing links with tracking parameters removed. Current selections: [Japan BOM](BOM_JP.md).

| Legacy item | Canonical source link | Original short annotation |
| --- | --- | --- |
| Camera | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=576963465018) | 160 degree |
| CSI to USB adapter | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=652556980724) |  |
| Acrylic board | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=598793410280) |  |
| Transparent silicone | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=547504169756) | transparent, 9345 |
| Transparent silicone | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=675851838980) |  |
| Translucent silicone | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=649539121020) | Shore 5A |
| Silicone to make the black gel layer | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=563842558717) |  |
| Black silicone pigment | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=631549311056) | Black |
| M2 heat-set threaded inserts | [Taobao / Tmall item](https://detail.tmall.com/item.htm?id=691362839974&skuId=5085575338790) | M2-5-3 |
| M2 screws for installing the sensor base | [Taobao / Tmall item](https://detail.tmall.com/item.htm?id=644136843341) | M2-6 |
| M3 nuts for installing the mold | [Taobao / Tmall item](https://detail.tmall.com/item.htm?id=556945578855) |  |
| M3 screws for installing the mold | [Taobao / Tmall item](https://detail.tmall.com/item.htm?id=587639753812) | M3-30 |
| Electronic scale | [Taobao / Tmall item](https://detail.tmall.com/item.htm?id=656617639991) |  |
| Glue gun | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=14332214805) |  |
| Soldering iron kit | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=676644094694) |  |
| Knife | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=734599732665) |  |
| Plastic cup | [Taobao / Tmall item](https://detail.tmall.com/item.htm?id=674497814902) |  |
| Stick | [Taobao / Tmall item](https://detail.tmall.com/item.htm?id=665681220554) |  |
| Dust removal paper | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=561103645534) |  |
| Plastic syringe | [Taobao / Tmall item](https://detail.tmall.com/item.htm?id=42062321347&skuId=4608584824303) |  |
| Glue (for the acrylic window) | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=725117394237) |  |
| Glue (for the black gel layer) | [Taobao / Tmall item](https://detail.tmall.com/item.htm?id=707070147914&skuId=4969702337602) |  |
| Vacuum pump | [Taobao / Tmall item](https://detail.tmall.com/item.htm?id=593806957297&skuId=4811795832968) | 28*28cm+8L or 6L+4L |
| Electric heating oven | [Taobao / Tmall item](https://item.taobao.com/item.htm?id=683283535428) |  |

## Changes in this handover

- Camera: builder purchased [Amazon JP B0C5W1QF65](https://www.amazon.co.jp/dp/B0C5W1QF65); selected variant still needs recording.
- Translucent silicone: builder chooses the **Shore 0** option at the original translucent-silicone link; the source document annotation says Shore 5A. Do not treat that old annotation as the current selection.
- Acrylic board: only the camera window is outsourced in acrylic, to Hazaiya. Casting molds are 3D printed; do not buy acrylic mold plates for this revision.
- LED board and white shell: reuse existing parts, marked ★ in the Japan BOM. For outsourced white shells, specify **White Nylon FS3300PA**; all other printed parts can use lab PLA.
- Lab-specific base/ring and LEAP mount files are in `hardware/`. Original mold DXF profiles and plate thicknesses are linked in **JP-29** of the [BOM](BOM_JP.md).
