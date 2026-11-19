# Fabrication handover

**English** · [日本語](HANDOVER.ja.md) · [Japan BOM](../bom/BOM_JP.md) · [Materials](MATERIALS.md)

Updated: 2026-11-19. “Builder-specified” records the builder's decisions; it does not imply that this documentation revision physically rebuilt or retested the sensor.

## What this build uses

This hardware companion to [9DTact](https://github.com/linchangyi1/9DTact) records modified parts, LEAP Hand integration and fabrication in Japan. Use upstream software for camera calibration, reconstruction and force-estimation workflows.

| Item | Hashimoto Lab decision | Handover detail |
| --- | --- | --- |
| Layer 2: translucent silicone | Same Taobao product, **Shore 0 option**, described by the builder as **Shore A 0**, replacing the original 5A selection | Actual package, mixing ratio and cure record still needed; a Japanese equivalent is not validated |
| Layer 3: silicone | [Builder-specified Amazon product](https://amzn.asia/d/08yFspH2) | Record exact package/model, mixing ratio and cure conditions |
| Layer 3: black pigment | [Builder-specified AliExpress product](https://ja.aliexpress.com/item/1005012698616201.html) | Record selected color, loading and resulting light blocking |
| Sensor base | `sensor_base_adapt_for_thick_PCB.STL` and `.SLDPRT` | Adapted for thicker camera PCB; STEP export and measured fit still needed |
| Isolation ring | `isolation_ring_out_11.4_in_10.3.STL` and `.SLDPRT` | Source and mesh now included; filename dimensions are not a fit measurement |
| LEAP attachment | `finger_tip_tactile_with_chip_holder.STL` and `finger_tip_tactile1_wrq.SLDPRT` | Derived from official LEAP CAD; the two local variants are not verified as a matching source/export pair |
| Camera | [Amazon Japan B0C5W1QF65](https://www.amazon.co.jp/dp/B0C5W1QF65) | Previously purchased by the builder; record the selected variant, PCB dimensions and lens |
| Acrylic window | Outsource the optical window to [Hazaiya](https://www.hazaiya.co.jp/) | Final drawing, thickness and tolerances still needed |
| Casting molds | **3D printed** | Do not order the original acrylic mold plates; actual mold files/settings still needed |
| ★ CSI–USB converter | **Reuse the existing board** | Matching replacement not found; skip procurement |
| ★ LED board | **Reuse the existing assembly** | Skip procurement; retain wiring, orientation and supply information |
| ★ White shell | **Reuse the existing shell; do not print in PLA** | Skip new fabrication; no substitute material is qualified here |

## Before fabrication

1. Identify the reused **CSI–USB board, LED board and white shell**, including cables and screws. Photograph board markings, connections and the assembled orientation.
2. Download the [three STL files](../hardware/README.md), confirm millimetre scale and dry-fit the camera PCB. Export STEP from the supplied SolidWorks files when needed for editable exchange.
3. Obtain the actual printed-mold files. If reconstructing them, check the shell, silicone thickness and sealing surfaces against the existing build. An upstream 2D DXF is not a printable solid mold.
4. Prepare the window drawing using the [Hazaiya outsourcing guide](WINDOW_OUTSOURCING.md). This repository does not contain a completed quote or purchase order.
5. Review the [BOM](../bom/BOM_JP.md) and [material notes](MATERIALS.md). Keep the builder's specified layer-3 links; test any replacement layer-2 silicone in small samples before use.

## Assembly and inspection sequence

This is an inspection sequence, not a verified timed casting recipe. Record actual mixing, degassing, curing and printing parameters rather than guessing missing values.

1. **Dry-fit the mechanics.** Check the camera PCB, base, lens, LED board, isolation ring and white shell without stressing the parts. Confirm screw head clearance, engagement and installed depth.
2. **Check the camera and lighting.** Use the existing CSI–USB board and LED assembly. Record camera mode, exposure, gain and focus; protect cables from pinching.
3. **Install the acrylic window.** Check the machined part against the shell and clean the optical surfaces. Test adhesive for bonding, fogging and compatibility with subsequent silicone curing.
4. **Cast layer 1: transparent silicone.** Preserve its transparent optical-medium function. The softer layer-2 material is not automatically a substitute for this layer.
5. **Cast and demold layer 2: translucent silicone.** Use the Taobao Shore 0 option. Check mold sealing, surface preparation, release and cure compatibility first. **Do not press or pull the silicone edge by hand; use a utility knife to carefully release the mold–silicone interface.** See the [demolding comparison](DEMOLDING.md).
6. **Cast and demold layer 3: black skin.** Use the specified [silicone](https://amzn.asia/d/08yFspH2) and [pigment](https://ja.aliexpress.com/item/1005012698616201.html), recording loading and cure conditions. Coat the required surface and sides for light blocking. **Use the same knife-assisted interface release; do not cut into the sensing surface or black skin.** Check adhesion and recovery after pressing.
7. **Mount to LEAP Hand.** Check fastening, full intended joint travel, interference, cable slack and strain relief before controlled motion. Modified-build screw sizes still need an actual fit check.
8. **Capture a new reference and recalibrate.** Follow [upstream calibration](https://github.com/linchangyi1/9DTact#3d-shape-reconstruction). Material/mechanical changes require renewed validation; do not assume an original force model retains its accuracy. Collect new data if needed.

## Handover acceptance record

| Check | Evidence to retain |
| --- | --- |
| Camera fixed without PCB stress | Dry-fit photographs and measured clearances |
| Stable no-contact image | Raw reference image and fixed exposure/gain settings |
| Contact visible centrally and near edges | Same test object at multiple positions |
| Response to ambient-light changes | Comparison under recorded lighting conditions |
| Recovery and intact skin after repeated contact | Cycle count, recovery time and photographs; lab-defined acceptance limits |
| LEAP motion without interference or cable pulling | Mounting details and motion video |
| Reproducible calibration | Source images, calibration files and software revision |

Use the [build-record template](BUILD_RECORD_TEMPLATE.md). Blank results are not passed checks.

## Next information to add

Priorities: printed-mold files, STEP exports, the final window drawing, Shore 0 packaging/recipe, layer-3 package details and pigment loading, print settings, camera variant, reused-board markings and LEAP fastening. See [known gaps](KNOWN_GAPS.md).

Six CAD/STL inputs are preserved byte-for-byte in this repository. The original files and source `9DTact_BOM.docx` remain unchanged in the parent handover folder.
