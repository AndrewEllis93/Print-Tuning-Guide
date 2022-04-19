[:arrow_left: Back to Table of Contents](/README.md)
# PA / EM Oddities
## Slight Perimeter Gapping
Some find that after tuning PA and EM, minor perimeter gapping is still present:

![](/images/perim-gapping-print.png)

Assuming EM is well tuned, this is often caused by a slight flow dropoff at higher print speeds — since most people print their perimeters faster than their top layer.

See [:page_facing_up:here](/articles/determining_max_volumetric_flow_rate.md#theory-vs-reality) for more information on flow dropoff.

There are a few different things you can do:\
*(in order of my preference)*
1. Use a hotend and/or nozzle (Bondtech CHT) with a higher flow ceiling.
    - This simply causes the flow dropoff to not start until a higher flow rate.
    - This can reduce the effect, but may not 100% fix it.
2. If your filament can handle it, increase hotend temperatures a bit. This also just helps with flow rates.
3. Increase your EM until the gaps dissappear. Then, lower your top layer flow (`fill_top_flow_ratio` in SS) until your top surfaces look perfect again.
4. Follow my [:page_facing_up:"determining maximum volumetric flow rate"](/articles/determining_max_volumetric_flow_rate.md#theory-vs-reality) instructions, and choose the "conservative" (always-100mm) value to enter into your slicer (PS/SS).
5. Slow your perimeters down. The faster you print, the greater this flow dropoff becomes.

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
1. Cover them up using single top perimeters (only available in SuperSlicer).
2. Slowly increase your EM until the gaps are covered. Then, lower your top layer flow (`fill_top_flow_ratio` in SS) until your top surfaces look perfect again.
3. Slow your perimeters down. The faster you print, the more pronounced these PA imperfections become.