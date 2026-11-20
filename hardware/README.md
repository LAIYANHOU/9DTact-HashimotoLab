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

**Planned:** Robotiq mounting adapter. / **今後追加予定：** Robotiq 用連結部品。

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

Use the lab's **PLA** for the base, ring, LEAP adapter, molds and calibration board. Reuse the white shell; outsourced replacements use **White Nylon FS3300PA**, not PLA. Record layer height, supports and orientation in the [build record](../docs/BUILD_RECORD_TEMPLATE.md).

## Molds and acrylic window

- **Molds:** extrude the original 9DTact DXF profiles to 2.5 / 2.8 / 3.0 mm, export STL and print. Source links: **JP-29** in the [BOM](../bom/BOM_JP.md).
- **Window:** transparent acrylic, outsourced to Hazaiya; final production drawing is still needed. See [window outsourcing](../docs/WINDOW_OUTSOURCING.md).
- **★ CSI–USB converter / ★ LED board / ★ white shell:** reuse existing assemblies.
- **Calibration board:** [original STL](https://github.com/linchangyi1/9DTact/blob/main/9DTact_Design/fabrication/calibration_board.STL); print in lab PLA.

## Upstream mapping

The base replaces upstream `fabrication/sensor_base.*`; the ring replaces `fabrication/isolation_ring.*`. The fingertips derive from official LEAP CAD. [Sources](../docs/SOURCES.md) · [Licenses](../LICENSE.md).
