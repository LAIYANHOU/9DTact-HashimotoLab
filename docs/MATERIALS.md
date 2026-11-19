# Silicone layers and material selection

**English** · [日本語](MATERIALS.ja.md) · [Handover](HANDOVER.md) · [Japan BOM](../bom/BOM_JP.md)

Builder-specified products updated: 2026-11-19. Japanese alternative-material research below was reviewed on 2026-11-18.

## Keep the three layers distinct

| Layer | Function | Material used or specified for this build |
| --- | --- | --- |
| **1 — transparent** | Transparent optical medium | Legacy BOM identifies transparent 9345 silicone; a Japanese equivalent is not yet qualified |
| **2 — translucent** | Deformable translucent sensing layer | Original [Taobao product](https://item.taobao.com/item.htm?id=649539121020), selecting **Shore 0**, described by the builder as **Shore A 0**; original BOM selection was 5A |
| **3 — black** | Light-blocking skin over the required contact surface and sides | [Builder-specified silicone on Amazon](https://amzn.asia/d/08yFspH2) plus [builder-specified black pigment on AliExpress](https://ja.aliexpress.com/item/1005012698616201.html) |

The third-layer links above replace the earlier generic sourcing suggestions in the active BOM. Product pages could not be fully retrieved during this update, so the brand/model, selected variant and recipe are not inferred from the URLs. Record them from the actual packages in the [build record](BUILD_RECORD_TEMPLATE.md).

**Identify the actual containers:** the builder confirmed that **layer 1** is the pair of white bottles with Huizhou labels and QR codes, **layer 2** is the pair marked **SHORE A 0**, and **layer 3** is the yellow/blue pair of jars. See the clickable photos in [BOM entries JP-04, JP-05 and JP-06](../bom/BOM_JP.md), or the [photo inventory](../assets/photos/README.md). Black pigment remains the separate JP-07 item; the third-layer jars are the silicone itself.

## Layer 2: recorded implementation

The builder selected the **Shore 0 option of the same Taobao listing** and has not purchased an equivalent second-layer silicone in Japan. The original Word BOM describes that listing as Shore 5A; that old annotation is not the selection for this build.

The exact Shore 0 model, cure chemistry, mixing ratio and optical data have not been archived. Preserve the builder's stated hardness, and do not automatically apply the old 5A product data to the 0 option.

## Layer 2: Japanese alternatives to investigate

**No Japan-sourced product has been validated as equivalent to the existing Taobao material.** The following are sample-testing or supplier-inquiry routes, not automatic substitutions.

| Candidate | Available evidence | What remains to check |
| --- | --- | --- |
| **Smooth-On Ecoflex 00-30** | Manufacturer describes a translucent silicone with **Shore 00-30** hardness; Japanese distributor has a product page | **00-30 is not the same designation as Shore A 0.** Compare optical response, deformation, recovery and bonding. [Japan product](https://sac-corp.myshopify.com/products/ecoflex-%EF%BD%B4%EF%BD%BA%EF%BE%8C%EF%BE%9A%EF%BD%AF%EF%BD%B8%EF%BD%BD-00-30-%EF%BE%84%EF%BE%97%EF%BD%B2%EF%BD%B1%EF%BE%99%EF%BD%B7%EF%BD%AF%EF%BE%84) · [Manufacturer](https://www.smooth-on.com/products/ecoflex-00-30/) |
| **Smooth-On Ecoflex 00-50** | Manufacturer describes translucent **Shore 00-50** silicone; Japanese distributor has a product page | The Japanese page also gives an approximate A-scale value, but this does not prove equivalence to the Taobao material. [Japan product](https://sac-corp.myshopify.com/products/ecoflex-00-50-%EF%BD%B4%EF%BD%BA%EF%BE%8C%EF%BE%9A%EF%BD%AF%EF%BD%B8%EF%BD%BD) · [Manufacturer](https://www.smooth-on.com/products/ecoflex-00-50/) |
| **Ytech / 株式会社ワイテック A0 materials and prototyping** | Its [material page](https://ytc-eng.com/silicon_syurui) lists two milky-white **Shore A 0** silicones, including a tacky type | These are materials for its fabrication services; raw A/B retail availability is unconfirmed. Ask about samples, raw material and optical properties |
| **Amazon Japan soft-silicone search** | [Shore 0A search](https://www.amazon.co.jp/s?k=Shore+0A+silicone) · [SANAAA search](https://www.amazon.co.jp/s?k=SANAAA+%E3%82%B7%E3%83%AA%E3%82%B3%E3%83%B3+0A) | A name such as “soft” or “gel” does not establish hardness, tear strength or suitability for tactile sensing |

Individual SAC Ecoflex pages displayed sold-out text in the 2026-11-18 review. A catalog page is not stock confirmation; confirm packaging and delivery with the supplier. [Japanese distributor catalog](https://sac-corp.co.jp/categories/additive_silicone.php).

If explicit A0 labeling is essential, Ytech is an inquiry route. If the lab needs a traceable material for small self-cast samples, Ecoflex is another test route, with different hardness designations and formulation. Neither route establishes equivalence without testing.

## Layer 3: specified products and batch record

- **Silicone:** use the [Amazon link supplied by the builder](https://amzn.asia/d/08yFspH2), recorded as **JP-06**.
- **Black pigment:** use the [AliExpress link supplied by the builder](https://ja.aliexpress.com/item/1005012698616201.html), recorded as **JP-07**.
- Record package/model, batch, selected color, A/B ratio, pigment loading, thickness and curing conditions. Check light blocking, adhesion and recovery on the assembled sensor.
- Demold using the lab's **utility-knife interface-release method**, also used for layer 2. [Illustrated procedure](DEMOLDING.md).

The original 9DTact design used Ecoflex 00-30 for its black skin. That historical choice does not identify the product behind the builder's new link, and does not identify this build's second-layer material.

## Small-sample replacement protocol

1. Keep existing Taobao material as a reference and cast comparison samples using the same mold geometry and thickness.
2. Follow each material's own manufacturer instructions. Record weights, mixing, temperature, degassing and cure. Do not transfer ratios between products or invent a softener-based “A0 recipe.”
3. Check cure compatibility on the actual mold material, surface finish and adhesive. [Smooth-On's instructions](https://www.smooth-on.com/products/ecoflex-00-30/) describe possible cure inhibition and small-scale compatibility testing.
4. Hold camera, LED, exposure and gain constant. Compare reference/contact images, transmission/scattering, residual deformation, recovery, tack, tearing and interlayer adhesion.
5. Promote a substitute to `lab_validated` only with a completed build record, mechanical checks and sensor validation. Recalibrate and separately evaluate force estimation.

The lab must define acceptance limits for its intended use. Unfilled records do not establish a passed material test.
