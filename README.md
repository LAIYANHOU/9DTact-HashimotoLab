# 9DTact-HashimotoLab

**A visual hardware handover for 9DTact + LEAP Hand, fabricated in Japan.**<br>
9DTact 硬體修改、LEAP Hand 固定件與實驗室製作交接。

[交接指南](docs/HANDOVER.zh-TW.md) · [BOM · English](bom/BOM_JP.md) · [BOM · 繁中](bom/BOM_JP.zh-TW.md) · [硬體下載](hardware/README.md) · [製作紀錄](docs/BUILD_RECORD_TEMPLATE.md)

![Three key parts: modified sensor base, isolation ring and LEAP fingertip mount](assets/mesh-preview.png)

This build adapts [9DTact](https://github.com/linchangyi1/9DTact) for the lab's camera PCB and LEAP Hand mounting. This companion repository collects the modified parts, fabrication choices and Japan sourcing notes; software and calibration remain upstream.

> **Handover in progress / 交接整理中** — All three important STL parts are included. Silicone, assembly and practical know-how photographs will be added by the builder. Japanese replacement materials and print settings still need physical validation.

## Three parts to know first / 三個重要零件

The numbers and colors below match the overview. Each STL link opens the actual mesh file; source CAD is linked separately.

| Part | What changed / 用途 | Files |
| --- | --- | --- |
| **01 · Sensor base** | Adapted for a **thicker camera PCB**／加厚 PCB 底座 | [STL](hardware/mesh/sensor_base_adapt_for_thick_PCB.STL) · [SolidWorks](hardware/cad/sensor_base_adapt_for_thick_PCB.SLDPRT) |
| **02 · Isolation ring** | Revised **camera light isolation** geometry／相機隔光環 | [STL](hardware/mesh/isolation_ring_out_11.4_in_10.3.STL) |
| **03 · LEAP fingertip mount** | Connects the tactile sensor to **LEAP Hand**, with a chip holder／含晶片固定位置 | [STL](hardware/mesh/finger_tip_tactile_with_chip_holder.STL) · [SolidWorks variant](hardware/cad/finger_tip_tactile1_wrq.SLDPRT) |

### 01 · Sensor base / 加厚 PCB 底座

The replacement base accommodates the builder's thicker camera PCB. Inspect the camera seat, fastener access and lens clearance before printing or assembling.

[![Sensor base: perspective, opposite side, face view and edge view](assets/parts/sensor-base.png)](hardware/mesh/sensor_base_adapt_for_thick_PCB.STL)

**Use:** [sensor_base_adapt_for_thick_PCB.STL](hardware/mesh/sensor_base_adapt_for_thick_PCB.STL)<br>
**Edit:** [SolidWorks source](hardware/cad/sensor_base_adapt_for_thick_PCB.SLDPRT) · STEP export still needed.

### 02 · Camera isolation ring / 相機隔光環

The revised ring is the light-isolation part around the camera optical path. Check its installed fit and the image near the sensing-area edges.

[![Camera isolation ring: perspective, opposite side, face view and edge view](assets/parts/isolation-ring.png)](hardware/mesh/isolation_ring_out_11.4_in_10.3.STL)

**Use:** [isolation_ring_out_11.4_in_10.3.STL](hardware/mesh/isolation_ring_out_11.4_in_10.3.STL)<br>
The filename is preserved; its numbers are not a substitute for checking the geometry and mating parts.

### 03 · LEAP fingertip mount / LEAP Hand 連接固定件

Modified from official LEAP Hand fingertip CAD to hold the tactile sensor. The supplied STL includes a chip holder. Check joint travel, cable clearance and the mounting screws on the actual hand.

[![LEAP fingertip with chip holder: perspective, opposite side, face view and edge view](assets/parts/leap-fingertip.png)](hardware/mesh/finger_tip_tactile_with_chip_holder.STL)

**Use:** [finger_tip_tactile_with_chip_holder.STL](hardware/mesh/finger_tip_tactile_with_chip_holder.STL)<br>
**Related editable variant:** [finger_tip_tactile1_wrq.SLDPRT](hardware/cad/finger_tip_tactile1_wrq.SLDPRT). The source/export relationship between these two variants has not been verified.

<details>
<summary><strong>360° rotating preview / 旋轉查看三個零件</strong></summary>

<img src="assets/parts-turntable.gif" alt="Rotating views of all three actual STL parts" width="1200">

</details>

All images are rendered from the **actual supplied STL files**. Parts are shown separately at independent scales. Views do not specify print orientation or demonstrate assembly fit. STL has no embedded units; confirm the intended millimetre scale in the slicer. [File hashes, bounds and provenance →](hardware/README.md)

## Fabrication at a glance / 製作路線

```mermaid
flowchart LR
    A[Review the 3 STL parts] --> B[Print custom parts and molds]
    B --> D[Cast silicone layers]
    C[Order acrylic window from Hazaiya] --> D
    D --> E[Assemble with reused LED and white shell]
    E --> F[Mount to LEAP and recalibrate]
```

| Item | Lab decision / 本版做法 | Go to |
| --- | --- | --- |
| **Camera** | Builder previously purchased **Amazon JP B0C5W1QF65**; record the selected variant and USB interface | [Camera product](https://www.amazon.co.jp/dp/B0C5W1QF65) |
| **Second silicone layer** | Original Taobao product, **Shore 0 option / Shore A 0**; replaces the original BOM's 5A option | [Material notes & Japan candidates](docs/MATERIALS.zh-TW.md) |
| **Acrylic window** | Outsource **only the optical window** to **はざいや / Hazaiya** | [Vendor](https://www.hazaiya.co.jp/) · [Drawing / quotation guide](docs/WINDOW_OUTSOURCING.zh-TW.md) |
| **Casting molds** | **3D print the molds**; do not order the original acrylic mold plates | [Mold files / settings to add](docs/KNOWN_GAPS.md) |
| **★ LED board** | **Reuse existing assembly — skip procurement** | [BOM](bom/BOM_JP.md) |
| **★ White shell** | **Reuse existing shell — do not print in PLA** | [Handover](docs/HANDOVER.zh-TW.md) |

Only the camera has builder-reported Amazon purchase evidence. Other Amazon search links are marked as sourcing routes. Japan silicone candidates are not yet qualified replacements. [Full BOM →](bom/BOM_JP.md)

## Demolding: a lab-specific change / 脫模方式修改

After **layer 2 (translucent)** and **layer 3 (black)**, we use a **utility knife to carefully release the mold–silicone interface**, instead of pressing or pulling the silicone edge by hand as shown in the [assembly tutorial](https://www.youtube.com/watch?v=VxMceWVz7QQ).

![Layer 2 and layer 3 demolding comparison: tutorial finger-pressure method on the left and utility-knife interface release on the right](assets/process/demolding-comparison.png)

**Follow the perimeter at the mold–silicone seam. Do not cut through the silicone or into the sensing surface.** The right panels are schematics; the red X marks the tutorial action replaced in this lab build. [English instructions / 繁中說明 →](docs/DEMOLDING.md)

第二層與第三層都不用手指壓開或拉開矽膠邊緣；改用美工刀沿模具與矽膠的交界小心分離。移除熱熔膠條是另一個步驟。

## Practical photographs / 實作照片待補

The builder will add real silicone and fabrication photographs. The CAD renders above cover the supplied geometry; they do not stand in for assembly photographs.

| Photo set | What the next builder should be able to see |
| --- | --- |
| **Assembled sensor & LEAP mount** | Final orientation, fastening and cable routing |
| **Camera / PCB fit** | PCB thickness, seating, screw access and lens clearance |
| **Three silicone layers** | Actual material packaging, Shore 0 selection and layer sequence |
| **Printed molds & casting** | Mold shape, surface preparation, sealing, demolding and common failures |
| **Finished contact surface** | Black coating and sides, good/failed examples, no-contact and contact images |

Photo filenames and caption guidance: [assets/photos/README.md](assets/photos/README.md). Add the actual settings and results to a [build record](docs/BUILD_RECORD_TEMPLATE.md).

## Build and hand over / 接手順序

1. Read the [Chinese handover](docs/HANDOVER.zh-TW.md); identify the reused LED board and white shell.
2. Download the **three STL parts**, confirm scale and dry-fit the camera. Obtain the lab's printed-mold files and settings.
3. Check the [Japan BOM](bom/BOM_JP.md), prepare the window drawing and test any replacement silicone in small samples.
4. Assemble, record the fabrication settings, test the LEAP mount through its intended motion, then recalibrate with [upstream 9DTact](https://github.com/linchangyi1/9DTact#3d-shape-reconstruction).

**Still to add:** mold files, STEP exports, the final window drawing, print/casting parameters and the builder's photographs. [Complete gap list →](docs/KNOWN_GAPS.md)

## Credit and file licenses

**9DTact:** Changyi Lin, Han Zhang, Jikai Xu, Lei Wu and Huazhe Xu. [Project](https://linchangyi1.github.io/9DTact/) · [Paper](https://arxiv.org/abs/2308.14277) · [Original fabrication files](https://github.com/linchangyi1/9DTact/tree/main/9DTact_Design/fabrication).

**LEAP Hand:** Kenneth Shaw, Ananye Agarwal and Deepak Pathak. [Project](https://v1.leaphand.com/) · [Official CAD terms](https://v1.leaphand.com/cad_request).

Licenses are scoped by file: original documentation/scripts and the 9DTact-derived base/ring use MIT terms. LEAP-derived fingertips retain their applicable upstream CAD terms; conflicting official license descriptions still need to be reconciled against the source download. [License scope](LICENSE.md) · [Attribution](NOTICE.md) · [Evidence sources](docs/SOURCES.md)

<details>
<summary>Repository layout and local checks</summary>

```text
hardware/cad/        SolidWorks source files
hardware/mesh/       Three important STL parts
hardware/manifest.json  Checksums, bounds and provenance
assets/parts/        Individual multi-view geometry sheets
assets/photos/      Guidance for the builder's future photographs
bom/                Japanese sourcing and original Taobao cross-reference
docs/               Handover, materials, window outsourcing and build records
scripts/            Inventory checks, BOM rendering and STL preview rendering
```

```bash
python3 scripts/verify_repository.py
python3 scripts/render_bom.py --check
# Optional: regenerate geometry figures (numpy, Pillow)
python3 scripts/render_mesh_preview.py --animate
```

These checks verify file integrity, local links and BOM consistency, rather than physical fit or material performance. Original files remain unchanged in the parent handover folder. The original Taobao Word document is not bundled here. [Publication notes](docs/PUBLISHING.md)

</details>
