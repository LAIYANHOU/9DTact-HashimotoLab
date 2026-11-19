# Hardware inventory / ハードウェア一覧

Three STL parts and three SolidWorks files. [Checksums and mesh dimensions](manifest.json).

| File | Purpose | Format / readiness |
| --- | --- | --- |
| [sensor_base_adapt_for_thick_PCB.STL](mesh/sensor_base_adapt_for_thick_PCB.STL) | **01 ·** Original 9DTact base, dimensions adjusted for thicker PCB | Print mesh |
| [sensor_base_adapt_for_thick_PCB.SLDPRT](cad/sensor_base_adapt_for_thick_PCB.SLDPRT) | Editable base | SolidWorks |
| [isolation_ring_out_11.4_in_10.3.STL](mesh/isolation_ring_out_11.4_in_10.3.STL) | **02 ·** Original 9DTact isolation ring, dimensions slightly adjusted | Print mesh |
| [isolation_ring_out_11.4_in_10.3.SLDPRT](cad/isolation_ring_out_11.4_in_10.3.SLDPRT) | Editable ring | SolidWorks |
| [finger_tip_tactile_with_chip_holder.STL](mesh/finger_tip_tactile_with_chip_holder.STL) | **03 ·** 9DTact-to-LEAP Hand adapter with chip holder | Print mesh |
| [finger_tip_tactile1_wrq.SLDPRT](cad/finger_tip_tactile1_wrq.SLDPRT) | Editable LEAP fingertip variant | SolidWorks |

![Supplied STL meshes](../assets/mesh-preview.png)

## Geometry inspection

| Mesh | Triangles | Coordinate extents X × Y × Z |
| --- | ---: | --- |
| Sensor base | 7,968 | 32.500 × 7.700 × 25.500 |
| Isolation ring | 586 | 11.300 × 2.800 × 11.400 |
| Chip-holder fingertip | 1,676 | 34.735 × 42.000 × 35.500 |

The table gives overall mesh bounds. Check millimetre scale in the slicer and measure mating features in CAD.

## Exporting for fabrication

Open STL files in a slicer. For STEP exchange, open the SolidWorks file, select the intended configuration and units, then export STEP. Match new exports to the required features, especially the fingertip chip holder.

Geometry sheets: [base](../assets/parts/sensor-base.png) · [ring](../assets/parts/isolation-ring.png) · [LEAP mount](../assets/parts/leap-fingertip.png) · [Rotating preview](../assets/parts-turntable.gif).

Record print material, layer height, supports and orientation in the [build record](../docs/BUILD_RECORD_TEMPLATE.md). **Reuse the white optical shell; do not print it in PLA.**

## Molds and acrylic window

- **Molds:** 3D printed; mold STL files still to be added.
- **Window:** transparent acrylic, outsourced to Hazaiya; final production drawing is still needed. See [window outsourcing](../docs/WINDOW_OUTSOURCING.md).
- **★ CSI–USB converter / ★ LED board / ★ white shell:** reuse existing assemblies.
- **Calibration board:** obtain the original file from [upstream fabrication](https://github.com/linchangyi1/9DTact/tree/main/9DTact_Design/fabrication) if recalibration is required.

## Upstream mapping

The base replaces upstream `fabrication/sensor_base.*`; the ring replaces `fabrication/isolation_ring.*`. The fingertips derive from official LEAP CAD. [Sources](../docs/SOURCES.md) · [Licenses](../LICENSE.md).
