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

The builder confirms that both `finger_tip_tactile1_wrq.SLDPRT` and `finger_tip_tactile_with_chip_holder.STL` were modified from official LEAP CAD to mount a tactile sensor; the STL variant includes a chip holder. The exact original CAD archive, revision, license copy and a detailed feature-level change log have not yet been supplied. The source/export relationship between these two local files has not been verified. The two official license descriptions currently differ; see [LICENSE.md](LICENSE.md).

## Original BOM and purchasing notes

The builder supplied `9DTact_BOM.docx` as a Taobao-oriented reference. The document is kept unchanged in the parent handover folder and not redistributed here. Factual specifications and cleaned product identifiers are cross-referenced in [bom/TAOBAO_REFERENCE.md](bom/TAOBAO_REFERENCE.md). No product screenshots or store images are copied into this repository.

Camera ASIN B0C5W1QF65, Hazaiya as a window supplier, Shore 0 from Taobao, printed molds, and reused CSI–USB/LED/shell are builder-reported facts. The builder later specified third-layer [silicone](https://amzn.asia/d/08yFspH2) and [pigment](https://ja.aliexpress.com/item/1005012698616201.html), confirmed shared tools, and supplied the isolation-ring SolidWorks source. Online candidates are labeled separately. No upstream author or supplier endorsement is implied.

## Demolding comparison

Assembly tutorial supplied by the builder: https://www.youtube.com/watch?v=VxMceWVz7QQ.

The composite `assets/process/demolding-comparison.png` uses two builder-supplied tutorial frames to identify finger-pressure release at the translucent and black demolding stages. The lab uses utility-knife release at the mold–silicone interface instead. Right-hand panels are generated schematics, not photographs of a performed operation. Comparison marks refer specifically to the lab's chosen procedure; they are not an endorsement or general rejection of the source tutorial. Underlying video stills retain their creators' rights. See [demolding instructions and figure provenance](docs/DEMOLDING.md).
