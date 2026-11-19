# Known gaps / 未完了項目

This is a status list, not a claim that the build has passed verification.

## Manufacturing

- [x] Include the builder-supplied isolation-ring `.SLDPRT` alongside its STL.

- [x] Include the builder-supplied `sensor_base_adapt_for_thick_PCB.STL` alongside its same-name SolidWorks source.
- [ ] Export the sensor base as STEP; verify its source configuration, STL scale and physical fit.
- [ ] Export the LEAP SolidWorks variant to STEP; determine whether it matches the supplied chip-holder STL or is a distinct variant.
- [ ] Add the **actual 3D printed mold files**, material, surface preparation, sealing method, release method, and successful print settings. Do not order acrylic molds from the original BOM.
- [ ] Add the camera-window manufacturing drawing, exact thickness, tolerances, and Hazaiya quotation specification.
- [ ] Record base, ring, and fingertip print materials, orientation, layer height, supports and post-processing. White shell: **no PLA; reuse**.
- [ ] Measure the camera PCB, lens clearance, mounting holes, installed ring and fasteners.
- [ ] Record LEAP hardware version, finger coverage, screw sizes and cable routing; verify full intended joint travel.

## Materials and procurement

- [x] Add builder-identified photographs of all three silicone pairs and the reused LED board to the BOM.
- [ ] Record readable material model/variant details and datasheets; record the actual mixing ratio, curing and degassing procedure. Packaging identification photographs are included.
- [ ] Validate a Japan-sourced second-layer silicone against the existing Taobao material.
- [ ] Record the purchased camera variant for Amazon JP ASIN B0C5W1QF65 and markings/pinout of the reused CSI–USB board; matching replacement not found.
- [ ] Replace Amazon **search-only** routes with exact checked product listings where possible; record shipping to Japan and variant.
- [ ] Confirm inserts by thread, body length, outside diameter and hole fit; the legacy `M2-5-3` notation is ambiguous without a drawing.
- [ ] Confirm quantities and screw head styles on the modified assembly; original-design counts are references only.
- [ ] Record quantities and identifiers of reusable ★ CSI–USB boards, ★ LED boards and ★ white shells.

## Validation and release

- [x] Record builder-specified layer-3 silicone/pigment links and confirmation of shared tools.
- [ ] Add assembly photos, no-contact/contact images, and a completed build record.
- [ ] Recalibrate after mechanical/material changes; separately validate any learned force model.
- [ ] Archive the license bundled with the original LEAP CAD download. The builder confirms both fingertip files derive from official CAD. On 2026-11-18, the current CAD access page says **CC BY-SA 4.0**, while the official API README says **CC BY-NC-SA**, without a version. Resolve which grant covers the source before public redistribution; do not blanket-license the fingertips as MIT.
- [x] Initial repository created and pushed by the builder: [LAIYANHOU/9DTact-HashimotoLab](https://github.com/LAIYANHOU/9DTact-HashimotoLab). Continue updating this existing remote; license provenance above still needs to be archived.

★ CSI–USB, ★ LED and ★ white shell procurement are intentionally deferred; completing a fresh fabrication workflow for them is outside this handover revision.
