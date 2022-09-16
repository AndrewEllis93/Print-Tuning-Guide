[:arrow_left: Back to Table of Contents](/README.md)

---
# Pressure Advance Tower Method

---

**I would highly recommend using the [:page_facing_up:lines method](/articles/pressure_advance.md#lines-method) rather than this method, if you can take some time to wrap your head around a small amount of g-code.** It is quicker and more precise. This "tower method" is here for beginners, and works, but is not my preferred method as it's a bit less precise.

This is based off of the [:page_facing_up:Klipper Pressure Advance guide](https://www.klipper3d.org/Pressure_Advance.html#tuning-pressure-advance), but with some modifications. 

The Klipper guide recommends limiting acceleration to 500 and square corner velocity (SCV) to 1, among other things. The intent behind these changes is to exaggerate the effects of pressure advance as much as possible. I'm not a fan of this approach.

In my opinion, it is best to run the calibration in close to normal printing conditions. This can make it slightly harder to tell the difference, but I find it more accurate.

---

**1)** Download and slice the [:page_facing_up:Klipper3d pressure advance tower STL](https://www.klipper3d.org/prints/square_tower.stl) with *your normal print settings (accelerations included)*. \
The only modifications you should make are these:

- **120mm/s** external perimeter speed
- **1** perimeter
- **0%** infill
- **0** top layers
- **0 second** "minimum layer time" / "layer time goal" / "slow down if layer print time is below"
    - Under filament cooling settings in PS/SS. 
    - You can use **ctrl+f** to find settings by name.
- **High fan speed**

**2)** Initiate the print.

**3)** After the print has *already started\**, enter the following command:

- (Direct Drive) `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.0025`
- (Bowden) `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.025`

You should now see increasing pressure advance values reporting to the g-code terminal as the print progresses.

<sup>\* *Certain patterns in your start g-code can cancel the tuning tower. \
\* It does not matter how quickly you enter the command, as it is based on height.*\
\* Alternatively, you can temporarily add the tuning tower command after your start g-code.</sup>

**4)** Allow the print to run until it starts showing obvious issues/gaps. Then you may cancel.

**5)** Measure the height of the perfect PA with calipers (see [:pushpin:images below](/articles/pressure_advance.md#example))
- Ensure you are **not** measuring your Z seam corner.
- There should be no signs of underextrusion before or after the corner. 
    - It can help to shine a bright flashlight between the walls.
- **It is normal for there to be a small amount of bulge on the trailing edge. When in doubt, choose the lower value.**
- If the height differs between corners, take a rough average.

**6)** Calculate your new pressure advance value:
- Multiply measured height by your `FACTOR`.
- Add the `START` value (usually just 0).

**8)** In the `[extruder]` section of your config, update `pressure_advance` to the new value and issue a `RESTART`.
- Alternatively, you can manage this per-filament by putting `SET_PRESSURE_ADVANCE ADVANCE=<value>` in your slicer's custom filament g-code.* 
    - Replace `<value>` with your desired PA.
    - \* *Unless you use Cura, which for some reason **still** doesn't support this basic functionality.*

**9)** Try printing something! 
- See [:pushpin:Fine-Tuning and What to Look For](/articles/pressure_advance.md#fine-tuning-and-what-to-look-for) to get an idea of what too high/low look like with actual prints.
- Tweaking in increments of 0.005 (with direct drive) is a good starting point.

### Example
**You may need to zoom in here, the differences are subtle.** There is always some ambiguity.

Excuse the gigantic photos - high resolution is needed here.

![](/images/PA-Tower.png) 
![](/images/PA-Tower-Annotated.png) 
---

[:arrow_left: Back to Table of Contents](/README.md)