# Attribution and provenance

## 9DTact

Original project: **9DTact: A Compact Vision-Based Tactile Sensor for Accurate 3D Shape Reconstruction and Generalizable 6D Force Estimation**, by Changyi Lin, Han Zhang, Jikai Xu, Lei Wu and Huazhe Xu.

- Source: https://github.com/linchangyi1/9DTact
- Fabrication: https://github.com/linchangyi1/9DTact/tree/main/9DTact_Design/fabrication
- License: https://github.com/linchangyi1/9DTact/blob/main/LICENSE
- Paper: https://arxiv.org/abs/2308.14277

This handover changes the sensor base for a thicker PCB, supplies a revised isolation ring, changes the second silicone layer to the builder's Taobao Shore 0 option, uses printed molds and a Japan acrylic-window vendor, and adds LEAP fingertip mounts. The software and calibration are referred to upstream rather than copied here. The upstream design was viewed at `main` on 2026-11-18; the exact upstream commit remains to be pinned.

## LEAP Hand

Original project: **LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning**, by Kenneth Shaw, Ananye Agarwal and Deepak Pathak (RSS 2023).

- Official project: https://v1.leaphand.com/
- CAD access and terms: https://v1.leaphand.com/cad_request
- Official API and CAD license description: https://github.com/leap-hand/LEAP_Hand_API

Both `finger_tip_tactile1_wrq.SLDPRT` and `finger_tip_tactile_with_chip_holder.STL` derive from official LEAP CAD; the STL includes a chip holder. [License details](LICENSE.md).

## Original BOM and purchasing notes

The builder supplied `9DTact_BOM.docx` as a Taobao-oriented reference. The document is kept unchanged in the parent handover folder and not redistributed here. Factual specifications and cleaned product identifiers are cross-referenced in [bom/TAOBAO_REFERENCE.md](bom/TAOBAO_REFERENCE.md).

Camera ASIN B0C5W1QF65, Hazaiya as a window supplier, Shore 0 from Taobao, printed molds, and reused CSI–USB/LED/shell are builder-reported facts. The builder later specified third-layer [silicone](https://amzn.asia/d/08yFspH2) and [pigment](https://ja.aliexpress.com/item/1005012698616201.html), confirmed shared tools, and supplied the isolation-ring SolidWorks source.

## Demolding comparison

Assembly tutorial supplied by the builder: https://www.youtube.com/watch?v=VxMceWVz7QQ.

The composite `assets/process/demolding-comparison.png` includes two builder-supplied tutorial frames and generated knife illustrations. Tutorial imagery retains its creators' rights.
