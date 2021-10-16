# THIS IS A WORK IN PROGRESS

# Introduction

Much of this guide is specific to Voron printers running Klipper. Rather than re-hashing concepts already described in Voron/Klipper documentation, I will be frequently linking to them and adding additional information and methods that utilize those concepts.

This is not intended to be an ultimate guide to everything, rather a guide to address common mistakes and confusion I see in the Voron Discord.

## A Note About Line Width
Any line widths expressed as percentages are referring to a **percentage of nozzle diameter.** \
This allows the guide to remain agnostic to nozzle diameter.

SuperSlicer natively allows percentages to be entered this way.

However: 
- Prusa Slicer bases percentages on layer heights instead. *(seriously, why?)*
- Cura does not allow percentages at all. 
- Other slicers may or may not support this.

**For Cura / Prusa Slicer / possibly others, you MUST use static line widths.** \
For example, enter **0.48mm** instead of **120%** if you are using a 0.4mm nozzle.
# Table of Contents
- [Extrusion Multiplier](#extrusion-multiplier)
- [First Layer Squish](#first-layer-squish)
- [Build Surface Adhesion](#build-surface-adhesion)
- [Pressure Advance](#pressure-advance)
- [Infill/Perimeter Overlap](#infill/perimeter-overlap-pinholes)
- [Retraction (WIP)](#retraction)
- [Cooling and Layer Times (WIP)](#cooling-and-layer-times)

# Extrusion Multiplier

This is a widely misunderstood and debated subject. Getting the perfect extrusion multiplier (EM) is *crucial* for good looking prints.

Some guides you will find online mention printing a single or two-walled object and measuring the thickness with calipers. I find this method not to work very well at all, especially with ABS, presumably due to shrinkage.

SuperSlicer has a built-in flow calibration tool, however I do not like this either, for a few reasons:
- It is very reliant on first layer squish.
- Because it uses 100% infill, the first layer squish carries through all the way to the top. 
- It has ironing turned on by default.
- The objects are too small. It's normal for smaller infill areas to look a bit more overextruded than larger infill areas.

Both of the above methods I've found to have error of up to 5% (sometimes even more) - which may not sound too bad but it makes a *huge* difference on the appearance of your prints.

This must be done per filament brand/type. It may vary by color or by roll, depending how consistent your filament brand of choice is. With KVP I am usually able to run the same EM for all colors.

## Method
By far the best method I have found is purely visual. *Put the calipers down for now*.

We will print some 30x30x3mm cubes. *(see the Test_Prints folder)*

**Print Settings:**
- **40+% Infill**\
    We need sparse infill rather than 100% solid infill, to remove the first layer squish from impacting the top layer. 
    We still need enough to adequately support the top layers.*
- **120% Infill [Line Width](#a-note-about-line-width)** \
    This just increases infill density over my normal settings, which are thicker for reducing print times.
- **100% Top Layer [Line Width](#a-note-about-line-width)**\
    This is more subject to interpretation, but I find 100% to have good results.
- **5 Top Layers**\
    This ensures that we have adequate support for the surface layer.
- **20-30mm/s Top Layer Speed**\
    This helps to remove pressure advance as a variable. The faster we go, the more pressure advance will impact our results.
- **0.03 Pressure Advance** (only if you have not yet tuned it)\
    This is simply a PA value on the lowest end of the normal range. 

**Steps:**

**1)** Print multiple test cubes with variations of 2% EM. You can do this all in once plate by adjusting settings for each object. Save it as a .3mf file for reuse later.

**2)** Inspect each cube. Once you are nearing the correct EM, the top should feel noticeably smoother. Too much EM will look and feel rougher, and too little EM will have gaps between the lines.

**3)** If desired, run the process again but with 0.5% intervals. Most PIF providers tune down to the 0.5% range, some even less. 

I have found that most ABS falls within the 91-94% range.

### Examples

This can be difficult to convey in photos. You may have to zoom in quite a bit to see the differences. It's easier to see in person - especially because you can manipulate the test prints and look at them in different lighting angles.\
You will get better at this through experience.
#### 2% Intervals
![](Images/EMPrints-Coarse.png) 
#### 0.5% Intervals
Now we run the print again at 0.5% intervals between the "too low" and "too high" examples from above.

Notice how the print becomes noticeably more shiny and glass-like around perfect EM (cube #3). 
This is not just a trick of the light. Shininess is not always the best indicator, but it makes a good visual example.

![](Images/EMPrints-Fine.png) 

#### Actual Print with Tuned EM:

![](Images/EMPrint-Example.jpg) 

# First Layer Squish

I'm going to call it "squish" for purposes of being unambiguous. \
"z offset" and "z height" can be conflated with other concepts. \
[It stops sounding like a real word after you type it 100 times.](https://en.wikipedia.org/wiki/Semantic_satiation)

## Background and Common Mistakes

- This section assumes that you have already done a rough [Z offset calibration](https://docs.vorondesign.com/build/startup/#initial--simple-process).

- This section also assumes that you have a *consistent* first layer. Here are some tips.
     - You may need to use [bed mesh](https://docs.vorondesign.com/tuning/secondary_printer_tuning.html#bed-mesh) to accomplish this. I personally recommend generating a bed mesh before every print, by adding `BED_MESH_CALIBRATE` to your `PRINT_START` macro. (requires the config section in the link above.)
        - Some discourage using bed mesh unless absolutely necessary, but I disagree. As far as I'm concerned, it's cheap insurance. Additionally, it's rare, especially for larger printers, to have a perfect first layer without it.
        - Your heat soaked mesh will also be different from your cold mesh, and will even vary at different temperatures, hence why I prefer to generate a fresh one for every print.

    - If you are using a V2: 
        - Ensure that you place your `BED_MESH_CALIBRATE` **after** G32, as G32 clears bed meshes by default.
        - Ensure that you are homing Z again after QGL, as QGL throws off Z height.

    - **(!) On larger enclosed printers (i.e. V2 & Trident), ensure that you are heat soaking for *at least* an hour.** \
    Z will drift upwards as the frame and gantry thermally expand with chamber heat. This can cause your first layer squish to vary between prints, and can even cause your first layer to drift up *as it prints*.

        Don't believe me? Look at this:

         ![](/Images/ZDrift.png)

        It's not ideal, but just get into a routine - start the heat soak from your phone when you wake up.

        There *are* ways around this - specifically by using gantry backers in combination with software-based frame thermal expansion compensation, but that is a rabbit hole well outside the scope of this guide.



## Method
**1)** Scatter square patches around your bed in your slicer. *(See Test_Prints folder)*

![](Images/FirstLayer-Plate.png)    

**2)** Set your first layer height to **0.25** or greater.

- Thinner first layer heights are considerably more sensitive and more difficult to maintain.

**3)** Set your first layer [line width](#a-note-about-line-width) to **120%** or greater.

**4)** Start the print. While it is printing, [live adjust z](https://docs.vorondesign.com/build/startup/#fine-tuning-z-height). Refer to the example images below.

- This can be done via gcodes/macros, LCD, or via web. I find it easiest to sit in front of the printer and fine-tune with the LCD.

**5)** Once you are happy with your squish, cancel the print and then save your new offset:

- V0/V2/Trident: 
    - Enter `Z_OFFSET_APPLY_ENDSTOP`. This will apply your new offset to your stepper_z's `position_endstop`.
- Switchwire/Legacy: 
    - Enter `Z_OFFSET_APPLY_PROBE`. This will apply your new offset to your probe's `z_offset`.
- Klicky Auto z: 
    - Manually adjust your `switch_offset`. Higher value = more squish.

## Examples 
You should still clearly be able to see the lines. If it's completely smooth, your squish is too much.
 If you see gaps between the lines, you need more squish.
### Good Squish
![](Images/FirstLayer-PrintExample.jpg) 
### Too Much Squish

![](Images/FirstLayer-TooMuchSquish1.png) 
![](Images/FirstLayer-TooMuchSquish2.png) 

### Not Enough Squish

![](Images/FirstLayer-NotEnoughSquish3.png) 

![](Images/FirstLayer-NotEnoughSquish1.png) 
![](Images/FirstLayer-NotEnoughSquish2.png) 


# Build Surface Adhesion

- **Smooth PEI:**
    - Scuff with some Scotch-Brite or a similarly rough pot scrubber or sandpaper.
    - Ensure that you actually *have* smooth PEI. Some spring steels, particularly the reverse side of some textured steels, are yellow/orange in appearance but do not actually have PEI applied. Inspect the edges of the plate to verify.

- **Textured PEI:**
    - Needs more squish than smooth PEI, to push the filament into the cracks/dimples.

- **(!) Thoroughly wash all build plates with dish soap and water, followed by 70+% isopropyl alcohol.**

- Avoid touching your build surface as much as possible. Oils from your fingers will cause issues. Handle your spring steel with a clean rag or cloth.

- Ensure your PEI is not counterfeit. You may have to ask in the Discord for other' experiences with a given brand. If your PEI is clear rather than yellowish, it's fake. This is particularly prevalent with random Amazon brands or unknown Aliexpress sellers.
# Pressure Advance

The Klipper guide recommends limiting acceleration to 500 and square corner velocity (SCV) to 1, among other things. 

The intent behind these changes is to exaggerate the effects of pressure advance as much as possible. In my opinion, it is best to run the calibration in close to normal printing conditions. This can make it slightly harder to tell the difference, but I find it more accurate.

Remember: *There is no such thing as perfect pressure advance*. Either accelerations or decelerations will always be slightly imperfect.

Pressure advance can change with different filaments. Typically I only find it necessary to tune per material type - ABS, PETG, PLA, TPU, etc.  I will only tune specific brands or colors of they are noticeably different.

With PS/SS, you can add a `SET_PRESSURE_ADVANCE ADVANCE=X` command to your filament profile's custom start g-code.
## Initial Calibration
This is based off of the [Klipper Pressure Advance guide](https://www.klipper3d.org/Pressure_Advance.html#tuning-pressure-advance), but with some modifications. 

**1)** Download and slice the [pressure advance tower](https://www.klipper3d.org/prints/square_tower.stl) with *your normal print setting (accelerations included)*. \
The only modifications you should make are these:

- **120mm/s perimeter speed**
- **1 perimeter**
- **0% infill**
- **0 top layers**
- **0 second "minimum layer time" / "layer time goal"**
- **High fan speed**

**2)** Initiate the print.

**3)** After the print has *already started\**, enter the following command:

- (Direct Drive) `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.0025`
- (Bowden) `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.025`

You should now see increasing pressure advance values reporting to the g-code terminal as the print progresses.

\* <sup>*Certain patterns in your start gcode can cancel the tuning tower. \
\* It does not matter how quickly you enter the command, as it is based on height.*</sup>

**4)** Allow the print to run until it starts showing obvious issues/gaps. Then you may cancel.

**5)** Measure the height of the perfect PA with calipers **(see images below)**
- Ensure you are **not** measuring your Z seam corner.
- There should be no signs of underextrusion before or after the corner. 
    - It can help to shine a bright flashlight between the walls.
- It is normal for there to be a small amount of bulge still. When in doubt, choose the lower value.
- If the height differs between corners, take a rough average.

**6)** Calculate your new pressure advance value:
- Multiply measured height by your `FACTOR`.
- Add the `START` value (usually just 0).

**8)** In the `[extruder]` section of your config, update `pressure_advance` to the new value.

**9)** Issue `RESTART` command.

### Example
**You may need to zoom in here, the differences are subtle.** There is always some ambiguity.

Excuse the gigantic photos - high resolution is needed here.

![](Images/PA-Tower.png) 
![](Images/PA-Tower-Annotated.png) 
## Fine-Tuning and What to Look For

The pressure advance tower method is usually good enough on its own, provided you measured correctly. This can take some experience, however, so here are some things to look out for.

Pressure advance **changes the distribution of material,** not the *amount* of material.
- Lower values cause less material in the middle of lines, and more at the ends/corners. 
- Higher values cause more material in the middle of lines, and less at the ends/corners.
### Pressure Advance is Too High
- Divots or underextrusion at corners and line ends.
- Gaps between perimeters at corners.

![](Images/PA-High-1.png) 

### Pressure Advance is Too Low
- Bulging at corners and line ends.
- Gaps between straight line perimeters.

![](Images/PA-Low-1.png) 

You can manually tweak pressure advance based on actual prints. Usually increments of 0.005 (with direct drive) are a good starting point.

# Infill/Perimeter Overlap

After tuning flow and pressure advance, you may still have some pinholes where your top infill meets your perimeters. This is more prevalent in PS/SS.

This is **not** necessarily an indicator that your flow or pressure advance are wrong, though they can impact it. 

Simply tweak "infill/perimeter overlap" (PS/SS) until satisfied.
## Pinholes
![](Images/Overlap-1.png) 
![](Images/Overlap-2.png) 

## Overlap Tweaked (40%)
![](Images/Overlap-Fixed1.png) 

## Regarding "Not Connected" Top Infill (SuperSlicer)

Some use "not connected" for their top infill. This does resolve the pinholes, however I find this to cause the opposite problem. It *overshoots.* 

To resolve this overshoot, you then need to *lower* your overlap. And because overlap is a global setting, this also starts to affect sparse infill/perimeter bonding - and therefore affects print strength.

# Retraction
WIP

# Cooling and Layer Times
WIP