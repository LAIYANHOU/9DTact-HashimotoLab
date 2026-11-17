# License scope

This repository is a hardware handover with mixed provenance. A license for one component does not relicense the other components.

| Files | Applicable terms |
| --- | --- |
| Original Markdown documentation, JSON procurement/inventory data, scripts and issue templates | MIT, [LICENSES/MIT.txt](LICENSES/MIT.txt) |
| `hardware/cad/sensor_base_adapt_for_thick_PCB.SLDPRT` | 9DTact-derived design; preserve [9DTact MIT notice](LICENSES/9DTact-MIT.txt); local adaptations offered under MIT |
| `hardware/mesh/isolation_ring_out_11.4_in_10.3.STL` | 9DTact-derived design; preserve [9DTact MIT notice](LICENSES/9DTact-MIT.txt); local adaptations offered under MIT |
| `hardware/cad/finger_tip_tactile1_wrq.SLDPRT`, `hardware/mesh/finger_tip_tactile_with_chip_holder.STL` | Derived from official LEAP CAD, as confirmed by the builder. **Original CAD grant/version needs confirmation; no new blanket license is assigned to these files.** See below |
| `assets/mesh-preview.png` | Contains renders of both the 9DTact ring and LEAP-derived fingertip; the respective underlying design terms continue to apply. It is not covered by the documentation MIT grant |
| Linked third-party products, sites, papers and upstream files | Their respective owners' terms; linking does not relicense them |

## LEAP CAD discrepancy to resolve

On 2026-11-18 the [official LEAP v1 CAD access page](https://v1.leaphand.com/cad_request) states **CC BY-SA 4.0** and links to [that license](https://creativecommons.org/licenses/by-sa/4.0/). The [official API README](https://github.com/leap-hand/LEAP_Hand_API) still describes CAD as **CC BY-NC-SA**, without identifying the version. Neither page identifies the exact source revision used to make the supplied fingertip files.

Archive the terms accompanying the builder's original CAD download, or obtain clarification that the current CC BY-SA 4.0 grant covers that source, before publicly redistributing the two fingertip files or their render. Retain attribution and describe the modifications. This draft preserves the files locally for lab handover; it does not declare that LEAP-derived CAD is MIT, commercially unrestricted, or fully cleared for public release.

9DTact's original MIT text is retained verbatim in `LICENSES/9DTact-MIT.txt`. The two local 9DTact hardware adaptations remain identifiable separately from LEAP-derived designs.
