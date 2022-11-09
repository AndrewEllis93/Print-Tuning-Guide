[:arrow_left: Back to Table of Contents](/README.md)

---
:first_quarter_moon: Marlin's version is called "linear advance", but the concepts are the same.

---
# PA / EM Oddities
## Slight Perimeter Gapping
Some find that after tuning PA and EM, minor perimeter gapping is still present:

![](/images/perim-gapping-print.png)

Assuming EM is well tuned, this is often caused by a slight [:page_facing_up:flow dropoff](/articles/determining_max_volumetric_flow_rate.md#flow-dropoff) at higher print speeds — since most people print their perimeters faster than their top layer.

There are a few different things you can try:\
*(in order of my preference)*
1. Ensure that you are not [:page_facing_up:outrunning your hotend](https://github.com/AndrewEllis93/Print-Tuning-Guide/blob/main/articles/determining_max_volumetric_flow_rate.md) and that you do not have a partial nozzle clog.
2. Take measures to improve your hotend's max flow rates.
    - **Higher flow ceilings allow for better extrusion consistency at lower flow rates**, as the [:page_facing_up:flow dropoff](/articles/determining_max_volumetric_flow_rate.md#flow-dropoff) curve starts later. It is beneficial for extrusion consistency at different speeds, **even when you don't intend to use the full flow rate.**
    - Try increasing hotend temperatures a bit.
        - Temperature can have a significant effect on max flow rates. 
        - Note: temp changes can have a minor effect on PA values.
    - Use a hotend and/or nozzle with a higher flow ceiling.
        - [:page_facing_up:Bondtech CHT](https://www.bondtech.se/product-category/nozzles/bondtech-nozzles/bondtech-cht/) and [:page_facing_up:Bozzle](https://www.fabreeko.com/products/bozzle-0-5mm-full-tungsten-carbide-nozzle-by-rentable-socks) both provide a sizeable flow rate increase to any hotend that supports V6 nozzles. CHT also has a Volcano variant.
    - These steps can reduce the effect, but may not 100% fix it.
5. Increase your EM until the gaps disappear. Then, lower your top layer flow (`fill_top_flow_ratio` in SS) until your top surfaces look perfect again.
6. Follow my [:page_facing_up:"determining maximum volumetric flow rate"](/articles/determining_max_volumetric_flow_rate.md) instructions, and choose the "conservative" (always-100mm) value to enter into your slicer (PS/SS).
7. Slow your perimeters down. The faster you print, the greater this flow dropoff becomes.

## Slight Corner Gapping

Having a finely tuned EM also unfortunately means that any cornering imperfections are **no longer hidden by overextrusion.** 

- ![](/images/corner-gapping-print.png)

Firstly, try to fine-tune PA to *reduce* the gaps as much as possible. They may not completely disappear, however. PA simply isn't perfect.

Here's an example.

- This is the "best" PA line from my test.

- The circled minor imperfections are the **exact same thing** that you are seeing in the image above.\
*(you may have to click the photo & zoom in)*
- ![](/images/corner-gapping.png)

There are a few different things you can do:\
*(in order of my preference)*
- Cover them up using single top perimeters (only available in SuperSlicer).
- Live with them! (within reason). 
    - Some corner gapping is just unavoidable when printing at speed, even with the "correct" pressure advance value, as evidenced in the above image.
- Try lowering your pressure advance smooth time a little bit. 
    - Don't go too low. There are diminishing returns. I run 0.02-0.025. Direct drive can handle lower than bowden. Too low will cause extruder skipping during PA movements.
- Slow your perimeters down. The faster you print, the more pronounced these PA imperfections become.
- These technically work, but are not my favored approaches. Some choose to do these and live with the drawbacks, however:
    - Lowering your pressure advance. This actually means running your PA *a bit too low* to force some extra material into the corners. 
        - **However, this can cause perimeter and top layer gapping. This likely also means having to overextrude a bit to compensate. Overextruding can affect dimensions and layer consistency.**
    - Increasing your extrusion multiplier until the gaps are covered. Then, lower your top layer flow (`fill_top_flow_ratio` in SS) until your top surfaces look good again. 
        - **This likely also means overextruding a bit to compensate. Overextruding can affect dimensions and layer consistency.**


---

[:arrow_left: Back to Table of Contents](/README.md)