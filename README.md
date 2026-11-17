# 9DTact-HashimotoLab

**9DTact hardware adaptations, LEAP Hand fingertips, and fabrication handover in Japan.**

[繁體中文交接指南](docs/HANDOVER.zh-TW.md) · [Japan BOM / 日本採購表](bom/BOM_JP.md) · [Hardware files](hardware/README.md) · [Build record](docs/BUILD_RECORD_TEMPLATE.md)

![Actual supplied STL meshes](assets/mesh-preview.png)

This repository records the Hashimoto Lab build of [9DTact](https://github.com/linchangyi1/9DTact). It focuses on the hardware changes and practical fabrication knowledge needed by the next lab member. Use the upstream repository for software and calibration.

**Status: initial handover draft, 2026-11-18.** The supplied CAD/STL files and the builder's decisions are preserved. Japanese replacement materials, missing manufacturing exports, and printing settings still need validation. This is not yet a fully reproduced build from a verified Japanese shopping list.

## What changed

| Area | Hashimoto Lab build | Evidence / files |
| --- | --- | --- |
| Second, translucent silicone layer | Taobao material, **Shore A 0** option, replacing the original BOM's Shore A 5 | Builder confirmed; exact product SKU and datasheet still needed |
| Sensor base | Adapted for a thicker camera PCB | [SolidWorks source](hardware/cad/sensor_base_adapt_for_thick_PCB.SLDPRT); STEP/STL export needed |
| Camera isolation ring | Revised ring | [STL](hardware/mesh/isolation_ring_out_11.4_in_10.3.STL) |
| LEAP Hand mounting | Modified official LEAP fingertip CAD, including a chip holder variant | [STL](hardware/mesh/finger_tip_tactile_with_chip_holder.STL), [SolidWorks source](hardware/cad/finger_tip_tactile1_wrq.SLDPRT); the two files are **not verified as the same revision** |
| Camera | Builder's previously purchased Amazon Japan item | [ASIN B0C5W1QF65](https://www.amazon.co.jp/dp/B0C5W1QF65); selected variant and USB interface need recording |
| Acrylic camera window | Outsource to **はざいや / Hazaiya** | [Vendor](https://www.hazaiya.co.jp/), [drawing quotation](https://www.hazaiya.co.jp/index.php/estimate-drawing); final window drawing needed |
| Casting molds | **3D printed**, rather than acrylic molds | Builder confirmed process; mold files and successful print settings not yet supplied |
| ★ LED board | **Reuse existing assembly; skip procurement in this handover** | Not replaced by a generic LED ring |
| ★ White sensor shell | **Reuse existing shell; do not print in PLA** | Optical/material requirements matter; no replacement material qualified here |

STL preview shows the two supplied meshes separately. It is not an assembly drawing, dimensional certification, or proof of fit. STL coordinates are provisionally interpreted as millimetres; confirm scale in the slicer.

## Start here

1. Read the [Chinese handover](docs/HANDOVER.zh-TW.md) and [known gaps](docs/KNOWN_GAPS.md).
2. Check the [hardware inventory](hardware/README.md). Export the base from SolidWorks before printing; obtain the lab's mold files.
3. Use the [Japan BOM](bom/BOM_JP.md). Only the camera is a builder-reported Amazon purchase. **Amazon search links are sourcing routes, not verified listings or approved substitutes.**
4. Keep the existing ★ LED board and ★ white shell. Order the acrylic window through Hazaiya using a checked drawing.
5. Record each silicone batch and print job in a [build record](docs/BUILD_RECORD_TEMPLATE.md), then validate the assembled sensor and recalibrate using upstream software.

## Repository layout

```text
hardware/cad/       Supplied SolidWorks sources
hardware/mesh/      Supplied STL files
hardware/manifest.json  Checksums, measured mesh bounds, provenance
bom/               Japanese sourcing table and Taobao cross-reference
docs/              Handover, material selection, window outsourcing, build records
assets/            Preview of actual supplied STL geometry
scripts/           Inventory verification and BOM rendering
LICENSES/          Scoped notices; see LICENSE.md
```

The original five input files remain untouched in the parent handover folder. The original Taobao `.docx` is source material there; it is not bundled into the public-source draft.

## Why a separate repository?

This is a focused companion to 9DTact rather than a fork of its complete software, datasets, and models. Upstream fabrication files remain [here](https://github.com/linchangyi1/9DTact/tree/main/9DTact_Design/fabrication). Our replacements and their provenance are listed explicitly. A companion repository also makes it easier to maintain Japanese procurement notes independently.

## Attribution and licenses

9DTact: Changyi Lin, Han Zhang, Jikai Xu, Lei Wu, and Huazhe Xu. [Project](https://linchangyi1.github.io/9DTact/) · [Paper](https://arxiv.org/abs/2308.14277).

LEAP Hand: Kenneth Shaw, Ananye Agarwal, and Deepak Pathak. [Project](https://v1.leaphand.com/) · [Official CAD access and terms](https://v1.leaphand.com/cad_request).

**Licenses are scoped by file, not blanket MIT.** Original documentation/scripts are MIT; the 9DTact-derived base and ring preserve the upstream MIT notice. LEAP-derived fingertips retain their applicable upstream CAD terms. The original LEAP CAD license supplied with the builder's download has not yet been archived; current official pages give conflicting terms. See [LICENSE.md](LICENSE.md) and [NOTICE.md](NOTICE.md) before redistribution or commercial use. Public release of these two fingertip files needs that discrepancy resolved.

## Contributing fabrication knowledge

For a replacement part, include the exact seller/SKU, selected variant, date, CAD revision, photos, and what was physically tested. A link found online alone does not establish compatibility. Use the issue templates for a fabrication result or sourcing update.

## Local checks

```bash
python3 scripts/verify_repository.py
python3 scripts/render_bom.py --check
```

These checks verify file integrity and documentation structure. They cannot establish physical fit, silicone performance, availability, or sensor accuracy.
