# THIS IS A WORK IN PROGRESS

# Introduction

Much of this guide is specific to Voron printers running Klipper. Rather than re-hashing concepts already described in Voron documentation, I will be frequently linking to it and adding additional information and methods that utilize those concepts.

Slicer screenshots are taken in SuperSlicer, but any concepts should directly translate to any slicer of your choosing.

This is not intended to be an ultimate guide to everything, rather a guide to address common mistakes and confusion I see in the Voron Discord.

**Any line widths expressed as percentages are referring to a percentage of nozzle width.** SuperSlicer allows percentages this way, however Prusa Slicer bases percentages on layer heights, and Cura does not allow percentages at all. For both, you must use static widths *(for example 120% w/ 0.4mm nozzle = 0.48mm)*
# Table of Contents
- [Extrusion Multiplier](#extrusion-multiplier)
- [First Layer Squish](#first-layer-squish)
- [Build Surface Adhesion](#build-surface-adhesion)
- [Pressure Advance](#pressure-advance)
- [Retraction](#retraction)
- [Cooling and Layer Times](#cooling-and-layer-times)

# Extrusion Multiplier

![](Images/EM.png)  

## Background


This is a widely misunderstood and debated subject. Getting the perfect extrusion multiplier (EM) is *crucial* for good looking prints.

Some guides you will find online mention printing a single or two-walled object and measuring the thickness with calipers. I find this method not to work very well at all, especially with ABS, presumably due to shrinkage.

SuperSlicer has a built-in flow calibration tool, however I do not like this either, for a few reasons:
- It is very reliant on first layer squish.
- Because it uses 100% infill, the first layer squish carries through all the way to the top. 
- It has ironing turned on by default.
- The objects are too small. It's normal for smaller infill areas to look a bit more overextruded than larger infill areas.

Both of the above methods I've found to have error of up to 5% Fsometimes even more) - which may not sound too bad but it makes a *huge* difference on the appearance of your prints.

## Method
By far the best method I have found is purely visual. *Put the calipers down for now*.

We will print some 30x30x3mm cubes. *(see the Test_Prints folder)*

**Print Settings:**
- **40+% Infill**\
    We need sparse infill rather than 100% solid infill, to remove the first layer squish from impacting the top layer. 
    We still need enough to adequately support the top layers.*
- **120% Infill Line Width**\
    This just increases infill density over my normal settings, which are thicker for reducing print times.
- **100% Top Layer Line Width**\
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

This image shows 0.5% intervals. Notice how the print becomes noticeably more shiny and glass-like around perfect EM (cube #3). This is not just a trick of the light. Shininess is not always the best indicator, but it makes a good visual example.

![](Images/EMPrints-Fine.png) 

Example of an actual print with tuned EM:

![](Images/EMPrint-Example.jpg) 

# First Layer Squish

## Background and Common Mistakes

- This section assumes that you have already done a rough [Z offset calibration](https://docs.vorondesign.com/build/startup/#initial--simple-process).

- This section also assumes that you have a *consistent* first layer. Here are some tips.
     - You may need to use [bed mesh](https://docs.vorondesign.com/tuning/secondary_printer_tuning.html#bed-mesh) to accomplish this. I personally recommend generating a bed mesh before every print, by adding `BED_MESH_CALIBRATE` to your `PRINT_START` macro. (requires the config section in the link above.)
        - Some discourage using bed mesh unless absolutely necessary, but I disagree. As far as I'm concerned, it's cheap insurance. Additionally, it's rare, especially for larger printers, to have a perfect first layer without it.
        - Your heat soaked mesh will also be different from your cold mesh, and will even vary at different temperatures, hence why I prefer to generate a fresh one for every print.

    - If you are using a V2: 
        - Ensure that you place your `BED_MESH_CALIBRATE` **after** G32, as G32 clears bed meshes by default.
        - Ensure that you are homing Z again after QGL, as QGL throws off Z height.

    - **On larger enclosed printers (i.e. V2 & Trident), ensure that you are heat soaking for *at least* an hour.** \
    Z will drift upwards as the frame and gantry thermally expand with chamber heat. This can cause your first layer squish to vary between prints, and can even cause your first layer to drift up *as it prints*:

    ![](/Images/ZDrift.png)

## Method
**1)** Scatter square patches around your bed in your slicer. *(See Test_Prints folder)*

![](Images/FirstLayer-Plate.png)    

**2)** Set your first layer height to **0.25** or greater.

- Thinner first layer heights are considerably more sensitive and more difficult to maintain.

**3)** Set your first layer line width to **120%** or greater.

**4)** Start the print. While it is printing, [live adjust z](https://docs.vorondesign.com/build/startup/#fine-tuning-z-height). Refer to the example images below.

- This can be done via gcodes/macros, LCD, or via web. I find it easiest to sit in front of the printer and fine-tune with the LCD.

**5)** Once you are happy with your squish, cancel the print and then save your new offset:

- V0/V2/Trident: 
    - Enter `Z_OFFSET_APPLY_ENDSTOP`. This will apply your new offset to your stepper_z's `position_endstop`.
- Switchwire/Legacy: 
    - Enter `Z_OFFSET_APPLY_PROBE`. This will apply your new offset to your probe's `z_offset`.
- Klicky Auto z: 
    - Manually adjust your `switch_offset`. Higher value = more squish.

### Examples (more to come): 

![](Images/FirstLayerPrint-Example.jpg) 

# Build Surface Adhesion

- **Smooth PEI:**
    - Scuff with some Scotch-Brite or a similarly rough pot scrubber or sandpaper.
    - Ensure that you actually *have* smooth PEI. Some spring steels, particularly the reverse side of some textured steels, are yellow/orange in appearance but do not actually have PEI applied. Inspect the edges of the plate to verify.

- **Textured PEI:**
    - Needs more squish than smooth PEI, to push the filament into the cracks/dimples.

- Thoroughly wash all build plates with dish soap and water, followed by 70+% isopropyl alcohol. **This is essential.**

- Avoid touching your build surface as much as possible. Oils from your fingers will cause issues. Handle your spring steel with a clean rag or cloth.

- Ensure your PEI is not counterfeit. You may have to ask in the Discord for other' experiences with a given brand. If your PEI is clear rather than yellowish, it's fake. This is particularly prevalent with random Amazon brands or unknown Aliexpress sellers.
# Pressure Advance

The Klipper guide recommends limiting acceleration to 500 and square corner velocity (SCV) to 1, among other things. 

The intent behind these changes is to exaggerate the effects of pressure advance as much as possible. I find that this actually throws off the results a small amount. In my opinion, it is best to run the calibration in close to normal printing conditions.
## Initial Calibration
This is based off of the [Klipper Pressure Advance guide](https://www.klipper3d.org/Pressure_Advance.html#tuning-pressure-advance), but with some modifications. 

**1)** Download and slice the [pressure advance tower](https://www.klipper3d.org/prints/square_tower.stl) with *your normal print setting (accelerations and speeds included)*. \
The only modifications you should make are these:

- **1 perimeter**
- **0% infill**
- **0 top layers**
- **0 second minimum layer time / layer time goal**
- **High fan speed**

**2)** Initiate the print.

**3)** After the print has *already started\**, enter the following command:

- (Direct Drive) `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.0025`
- (Bowden) `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.025`

\* <sup>*Certain patterns in your start gcode can cancel the tuning tower.*</sup>

**4)** Allow the print to run until it starts showing obvious issues. Then you may cancel.

**5)** Following the [Klipper guide](https://www.klipper3d.org/Pressure_Advance.html#tuning-pressure-advance), measure the height of the perfect PA with calipers.
- Ensure you are **not** measuring your Z seam corner.
- There should be no signs of divots before or after the corner. 
- It is normal for there to be a small amount of bulge still. When in doubt, choose the lower value.
- If the height differs between corners, take a rough average.

**6)** Calculate your new pressure advance value:
- Multiply measured height by your `FACTOR`.
- Add the `START` value (usually just 0).

**8)** In the `[extruder]` section of your config, update `pressure_advance` to the new value.

**9)** Issue `RESTART` command.
## Fine-Tuning

The pressure advance tower method is usually good enough on its own.

It takes some experience to manually tweak it. Usually increments of 0.005 (with direct drive) are a good starting point.

Pressure advance **changes the distribution of material,** not the *amount* of material.
- Lower values cause less material in the middle of lines, and more at the ends/corners. 
- Higher values cause more material in the middle of lines, and less at the ends/corners.
### Pressure Advance is Too High
- Divots or underextrusion at corners and line ends.
- Gaps between corners perimeters.

![](Images/PA-High-1.png) 

### Pressure Advance is Too Low
- Bulging at corners and line ends.
- Gaps between straight perimeters.

![](Images/PA-Low-1.png) 
# Retraction
WIP

# Cooling and Layer Times
WIP