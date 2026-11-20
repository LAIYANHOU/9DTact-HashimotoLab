# Sources / 参考資料

Online references reviewed on 2026-11-18; builder updates added on 2026-11-19–20.

## Builder-provided evidence

- Six local hardware files, preserved byte-for-byte; [checksums and inventory](../hardware/manifest.json).
- Original `9DTact_BOM.docx`, retained in the parent folder; [24 cleaned source product references](../bom/TAOBAO_REFERENCE.md).
- On 2026-11-20, the builder selected Ecoflex 00-30 as the provisional layer-2 substitute, using the same Amazon product as layer 3. It is untested for layer 2; closeness to the previous Taobao Shore 0A material is the builder’s expectation.
- Layer 1: the builder estimates approximately Shore 45 and reports that Japanese stock has not been found; no procurement link is listed.
- Four original lab photographs supplied and identified by the builder on 2026-11-19: layer-1 Huizhou/QR-code bottles (JP-04), layer-2 “SHORE A 0” bottles (JP-05), layer-3 yellow/blue jars (JP-06), and reused LED board (JP-24). See the [photo inventory](../assets/photos/README.md).
- Camera previously purchased: [Amazon Japan ASIN B0C5W1QF65](https://www.amazon.co.jp/dp/B0C5W1QF65).
- Acrylic camera window can be outsourced to [Hazaiya](https://www.hazaiya.co.jp/); other molds are 3D printed.
- Existing CSI–USB board, LED board and white shell are reused. A matching CSI–USB replacement was not found. For outsourced white shells, the builder specifies **White Nylon FS3300PA**; the lab's PLA can be used for all other printed parts.
- On 2026-11-19, the builder specified [layer-3 silicone](https://amzn.asia/d/08yFspH2) and [black pigment](https://ja.aliexpress.com/item/1005012698616201.html) and confirmed shared tools.
- Builder-supplied isolation-ring SolidWorks source was added on 2026-11-19; its exact bytes are in the hardware manifest.
- Both local LEAP fingertip files derive from official LEAP CAD.
- Demolding layers 2 and 3: builder specifies careful utility-knife release along the mold–silicone interface, replacing hand pressure/pulling at the edge. The builder supplied [the assembly tutorial](https://www.youtube.com/watch?v=VxMceWVz7QQ) and screenshots showing both demolding stages. See the [comparison figure](../assets/process/demolding-comparison.png).

- On 2026-11-20, the builder supplied eight JP-labelled screenshots, the selected Amazon links for JP-08–11, and the original shell/calibration-board STL links. The screenshots are preserved unchanged in `assets/bom/`; JP-10 and JP-11 share one image.
- [Calibration-board preview](../assets/bom/calibration-board.png): rendered directly from the [original STL](https://github.com/linchangyi1/9DTact/blob/main/9DTact_Design/fabrication/calibration_board.STL). The source checksum is recorded in [BOM data](../bom/bom_jp.json).

## Original 9DTact design

- [Official repository](https://github.com/linchangyi1/9DTact): project attribution, software and calibration workflow.
- [Fabrication directory](https://github.com/linchangyi1/9DTact/tree/main/9DTact_Design/fabrication): reference base/ring, molds and calibration-board files.
- [Design directory](https://github.com/linchangyi1/9DTact/tree/main/9DTact_Design): module and assembly references.
- [Official MIT license](https://raw.githubusercontent.com/linchangyi1/9DTact/main/LICENSE): retrieved text preserved in `LICENSES/9DTact-MIT.txt`.
- [9DTact paper, sensor design and BOM](https://arxiv.org/html/2308.14277v2#S3): baseline camera, three gel layers, original fastener counts and acrylic-window thickness.

## Japanese procurement and material references

- [Hazaiya drawing quotation](https://www.hazaiya.co.jp/index.php/estimate-drawing): lists `.dxf`, `.ai` and `.svg` uploads. [Machining order page](https://www.hazaiya.co.jp/estimate): process options.
- [SAC silicone catalog](https://sac-corp.co.jp/categories/additive_silicone.php): Japanese source for Smooth-On materials.
- [Smooth-On Ecoflex 00-30](https://www.smooth-on.com/products/ecoflex-00-30/): manufacturer material reference.
- [SAC Silc-PIG](https://sac-corp.myshopify.com/products/silc-pig-9%E3%82%AB%E3%83%A9%E3%83%BC%E3%82%B5%E3%83%B3%E3%83%97%E3%83%A9%E3%83%BC) and [Smooth-On Silc Pig](https://www.smooth-on.com/products/silc-pig/): pigment sourcing and silicone compatibility. Exact black package and dosing require checking.
- [SAC Sil-Poxy](https://sac-corp.myshopify.com/products/sil-poxy): silicone bonding and repair adhesive.
- [HAKKO FX600](https://www.hakko.com/japan/products/hakko_fx600.html): primary reference for a Japanese temperature-controlled soldering-iron candidate.

## LEAP CAD attribution and conflicting license descriptions

- [Official LEAP v1 CAD access page](https://v1.leaphand.com/cad_request): live page reviewed on 2026-11-18 states CC BY-SA 4.0, allowing commercial adaptations under attribution/share-alike terms.
- [Official LEAP API README](https://github.com/leap-hand/LEAP_Hand_API): reviewed description states CAD is CC BY-NC-SA, without a version.

See [license details](../LICENSE.md) for the LEAP source-license record.
