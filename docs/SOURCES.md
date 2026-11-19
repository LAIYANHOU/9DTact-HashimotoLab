# Sources and evidence / 來源與查核範圍

Reviewed on 2026-11-18. The distinction between builder reports, source documents and proposed engineering checks is intentional.

## Builder-provided evidence

- Six local hardware files, preserved byte-for-byte; [checksums and inventory](../hardware/manifest.json).
- Original `9DTact_BOM.docx`, retained in the parent folder; [24 cleaned source product references](../bom/TAOBAO_REFERENCE.md).
- Second-layer material: original Taobao translucent-silicone product, selected Shore 0 option; builder describes it as Shore A 0. No Japanese purchase of this material.
- Camera previously purchased: [Amazon Japan ASIN B0C5W1QF65](https://www.amazon.co.jp/dp/B0C5W1QF65).
- Acrylic camera window can be outsourced to [Hazaiya](https://www.hazaiya.co.jp/); other molds are 3D printed.
- Existing CSI–USB board, LED board and white shell are reused. A matching CSI–USB replacement was not found. White shell must not be PLA.
- On 2026-11-19, the builder specified [layer-3 silicone](https://amzn.asia/d/08yFspH2) and [black pigment](https://ja.aliexpress.com/item/1005012698616201.html) and confirmed shared tools. Product pages could not be fully retrieved; no model or recipe is inferred from those links.
- Builder-supplied isolation-ring SolidWorks source was added on 2026-11-19; its exact bytes are in the hardware manifest.
- Both local LEAP fingertip files derive from official LEAP CAD.
- Demolding layers 2 and 3: builder specifies careful utility-knife release along the mold–silicone interface, replacing hand pressure/pulling at the edge. The builder supplied [the assembly tutorial](https://www.youtube.com/watch?v=VxMceWVz7QQ) and screenshots showing both demolding stages. The video page could not be played during this review; visible screenshot captions and the builder's explanation establish the comparison. See [DEMOLDING.md](DEMOLDING.md).

## Original 9DTact design

- [Official repository](https://github.com/linchangyi1/9DTact): project attribution, software and calibration workflow.
- [Fabrication directory](https://github.com/linchangyi1/9DTact/tree/main/9DTact_Design/fabrication): reference base/ring, molds and calibration-board files. No original files from this directory were copied into this draft.
- [Design directory](https://github.com/linchangyi1/9DTact/tree/main/9DTact_Design): module and assembly references.
- [Official MIT license](https://raw.githubusercontent.com/linchangyi1/9DTact/main/LICENSE): retrieved text preserved in `LICENSES/9DTact-MIT.txt`.
- [9DTact paper, sensor design and BOM](https://arxiv.org/html/2308.14277v2#S3): baseline camera, three gel layers, original fastener counts and acrylic-window thickness. These baseline details do not establish modified-build dimensions or new-material performance.

The upstream repository was viewed at `main`; a specific commit hash could not be obtained through the available connection. Pin it when adding an upstream manufacturing snapshot.

## Japanese procurement and material references

- [Hazaiya drawing quotation](https://www.hazaiya.co.jp/index.php/estimate-drawing): lists `.dxf`, `.ai` and `.svg` uploads. [Machining order page](https://www.hazaiya.co.jp/estimate): process options. This establishes a quotation route, not a completed order or accepted tolerance.
- [SAC silicone catalog](https://sac-corp.co.jp/categories/additive_silicone.php): Japanese source for Smooth-On materials. A catalog listing is not stock confirmation.
- [SAC Ecoflex 00-30](https://sac-corp.myshopify.com/products/ecoflex-%EF%BD%B4%EF%BD%BA%EF%BE%8C%EF%BE%9A%EF%BD%AF%EF%BD%B8%EF%BD%BD-00-30-%EF%BE%84%EF%BE%97%EF%BD%B2%EF%BD%B1%EF%BE%99%EF%BD%B7%EF%BD%AF%EF%BE%84) and [Ecoflex 00-50](https://sac-corp.myshopify.com/products/ecoflex-00-50-%EF%BD%B4%EF%BD%BA%EF%BE%8C%EF%BE%9A%EF%BD%AF%EF%BD%B8%EF%BD%BD): Japanese product pages; both displayed sold-out text during review. Availability of each pack/variant remains unconfirmed.
- [Smooth-On Ecoflex 00-30](https://www.smooth-on.com/products/ecoflex-00-30/) and [Ecoflex 00-50](https://www.smooth-on.com/products/ecoflex-00-50/): primary hardness, appearance and handling references. Neither establishes equivalence to the builder's Taobao Shore 0 silicone.
- [Ytech / 株式会社ワイテック material page](https://ytc-eng.com/silicon_syurui): explicitly lists milky-white Shore A 0 silicones for its casting/prototyping services. Raw A/B retail availability, Amazon availability, optical equivalence and fit to this sensor are unconfirmed; this is an inquiry route.
- [SAC Silc-PIG](https://sac-corp.myshopify.com/products/silc-pig-9%E3%82%AB%E3%83%A9%E3%83%BC%E3%82%B5%E3%83%B3%E3%83%97%E3%83%A9%E3%83%BC) and [Smooth-On Silc Pig](https://www.smooth-on.com/products/silc-pig/): pigment sourcing and silicone compatibility. Exact black package and dosing require checking.
- [SAC Sil-Poxy](https://sac-corp.myshopify.com/products/sil-poxy): a possible silicone-repair adhesive, not a validated replacement for every legacy adhesive.
- [HAKKO FX600](https://www.hakko.com/japan/products/hakko_fx600.html): primary reference for a Japanese temperature-controlled soldering-iron candidate.

Amazon Japan product pages could not be fully retrieved in this review. The camera link has builder-reported purchase evidence; the layer-3 links are builder-specified, and shared tools are builder-confirmed. All `/s?k=…` links are explicitly labeled **search routes**; seller, SKU, selected variant, price, stock and compatibility are not verified. General tool selection notes are proposed engineering guidance, not reports of successful lab use.

## LEAP CAD attribution and conflicting license descriptions

- [Official LEAP v1 CAD access page](https://v1.leaphand.com/cad_request): live page reviewed on 2026-11-18 states CC BY-SA 4.0, allowing commercial adaptations under attribution/share-alike terms.
- [Official LEAP API README](https://github.com/leap-hand/LEAP_Hand_API): reviewed description states CAD is CC BY-NC-SA, without a version.

These do not identify the exact source file used by the builder. The applicable original grant must be recorded rather than inferred from a blanket repository license. See [license scope](../LICENSE.md).
