# License scope

| Files | Applicable terms |
| --- | --- |
| Original Markdown documentation, JSON procurement/inventory data, scripts and issue templates | MIT, [LICENSES/MIT.txt](LICENSES/MIT.txt) |
| `hardware/cad/sensor_base_adapt_for_thick_PCB.SLDPRT` | 9DTact-derived design; preserve [9DTact MIT notice](LICENSES/9DTact-MIT.txt); local adaptations offered under MIT |
| `hardware/mesh/sensor_base_adapt_for_thick_PCB.STL` | 9DTact-derived base mesh, supplied by the builder; preserve [9DTact MIT notice](LICENSES/9DTact-MIT.txt); local adaptations offered under MIT |
| `hardware/cad/isolation_ring_out_11.4_in_10.3.SLDPRT` | 9DTact-derived ring source supplied by the builder; preserve [9DTact MIT notice](LICENSES/9DTact-MIT.txt); local adaptations offered under MIT |
| `hardware/mesh/isolation_ring_out_11.4_in_10.3.STL` | 9DTact-derived design; preserve [9DTact MIT notice](LICENSES/9DTact-MIT.txt); local adaptations offered under MIT |
| `hardware/cad/finger_tip_tactile1_wrq.SLDPRT`, `hardware/mesh/finger_tip_tactile_with_chip_holder.STL` | Derived from official LEAP CAD, as confirmed by the builder. **Original CAD grant/version needs confirmation; no new blanket license is assigned to these files.** See below |
| `assets/mesh-preview.png`, `assets/parts-turntable.gif`, `assets/parts/*.png` | Contain renders of the 9DTact-derived base/ring and/or LEAP-derived fingertip; the respective underlying design terms continue to apply. It is not covered by the documentation MIT grant |
| Linked third-party products, sites, papers and upstream files | Their respective owners' terms; linking does not relicense them |
| `assets/process/demolding-comparison.png` | Includes builder-supplied stills from the linked assembly tutorial and generated explanatory diagrams. The underlying tutorial imagery retains its creators' rights; no new MIT grant is asserted for this composite |

## LEAP CAD discrepancy to resolve

On 2026-11-18 the [official LEAP v1 CAD access page](https://v1.leaphand.com/cad_request) states **CC BY-SA 4.0** and links to [that license](https://creativecommons.org/licenses/by-sa/4.0/). The [official API README](https://github.com/leap-hand/LEAP_Hand_API) still describes CAD as **CC BY-NC-SA**, without identifying the version. Neither page identifies the exact source revision used to make the supplied fingertip files.

Archive the terms accompanying the builder's original CAD download, or obtain clarification that the current CC BY-SA 4.0 grant covers that source. Retain attribution and describe the modifications.

9DTact's original MIT text is retained verbatim in `LICENSES/9DTact-MIT.txt`. The two local 9DTact hardware adaptations remain identifiable separately from LEAP-derived designs.
