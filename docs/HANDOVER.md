# Fabrication handover

[日本語](HANDOVER.ja.md) · [BOM](../bom/BOM_JP.md)

This build makes small dimensional adjustments to the original [9DTact](https://github.com/linchangyi1/9DTact) base and isolation ring, and adds a LEAP Hand mounting adapter. Use upstream software for calibration, reconstruction and force estimation.

## Start with the original video

[![▶ 9DTact Fabrication Tutorial](https://i.ytimg.com/vi/VxMceWVz7QQ/hqdefault.jpg)](https://www.youtube.com/watch?v=VxMceWVz7QQ)

[▶ Watch the 9DTact Fabrication Tutorial](https://www.youtube.com/watch?v=VxMceWVz7QQ), then follow the build configuration and assembly steps below for the Hashimoto Lab version.

## Build configuration

| Item | Hashimoto Lab build |
| --- | --- |
| Layer 1 | Clear 9345 silicone; white Huizhou/QR-code bottles |
| Layer 2 | Taobao **Shore A 0**, replacing 5A; bottles marked “0” |
| Layer 3 | [Silicone](https://amzn.asia/d/08yFspH2) in yellow/blue jars + [black pigment](https://ja.aliexpress.com/item/1005012698616201.html) |
| Sensor base | [Thicker-PCB base, STL + SolidWorks](../hardware/README.md) |
| Isolation ring | [Revised ring, STL + SolidWorks](../hardware/README.md) |
| LEAP attachment | [Chip-holder STL and SolidWorks variant](../hardware/README.md), modified from official LEAP CAD |
| Camera | [Amazon Japan B0C5W1QF65](https://www.amazon.co.jp/dp/B0C5W1QF65) |
| Acrylic window | Outsource to [Hazaiya](WINDOW_OUTSOURCING.md) |
| Casting molds | **3D print** |
| ★ CSI–USB converter, LED board, white shell | **Reuse existing parts. Do not print the white shell in PLA.** |

Material and LED identification photos are in the [BOM](../bom/BOM_JP.md).

## Before fabrication

1. Gather the reused assemblies, cables and fasteners.
2. Download the [STL files](../hardware/README.md), check millimetre scale and dry-fit the camera PCB.
3. Obtain the mold files and prepare the [window drawing](WINDOW_OUTSOURCING.md).
4. Prepare the materials and tools in the [BOM](../bom/BOM_JP.md).

## Assembly

1. **Dry-fit the mechanics.** Check PCB seating, lens clearance, LED board, isolation ring, shell and screw engagement.
2. **Check camera and lighting.** Connect the existing CSI–USB board and LED assembly. Set exposure, gain and focus; route cables clear of clamping surfaces.
3. **Install the acrylic window.** Clean the optical faces and check the adhesive seal, bonding and fogging.
4. **Cast layer 1.** Use the transparent silicone.
5. **Cast and demold layer 2.** Use [Shore A 0](MATERIALS.md). **Release the mold–silicone interface with a utility knife instead of pressing or pulling the edge by hand.** [Illustrated procedure](DEMOLDING.md).
6. **Cast and demold layer 3.** Add black pigment to the specified silicone, covering the contact surface and required sides. Use the same knife-assisted release; **keep the sensing surface and black skin intact**.
7. **Mount to LEAP Hand.** Check screws, joint travel, interference and cable slack.
8. **Capture a new reference and recalibrate.** Follow [upstream calibration](https://github.com/linchangyi1/9DTact#3d-shape-reconstruction); evaluate force-estimation accuracy after the changes.

Record mixing, degassing, curing and print settings in the [build record](BUILD_RECORD_TEMPLATE.md).

## Final checks

| Check | Keep with the build record |
| --- | --- |
| Stable no-contact image | Raw image, exposure and gain |
| Contact response at the centre and edges | Test images and object details |
| Recovery and intact skin after repeated contact | Cycle count, recovery time and photos |
| LEAP motion without interference or cable pulling | Mounting photos and motion video |
| Calibration and force estimation | Software revision, data and measured error |

[Remaining files and parameters to add →](KNOWN_GAPS.md)
