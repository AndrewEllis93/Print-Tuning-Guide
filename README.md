This documentation is a work in progress.


If you have issues, comments, or suggestions, please let me know on Discord: [Ellis#4980](https://discordapp.com/users/207622442842062849)
# Introduction

Much of this guide is specific to Voron printers running Klipper. Rather than re-hashing concepts already described in Voron/Klipper documentation, I will be frequently linking to them and adding additional information and methods that utilize those concepts.

This is not intended to be an ultimate guide to everything, rather a guide to address common mistakes and confusion I see in the Voron Discord.

My SuperSlicer profiles are located [here](https://github.com/AndrewEllis93/Ellis-PIF-Profile).

Thank you to **bythorsthunder** for help with testing these methods and providing some of the photos.

# Table of Contents
- [A Note About Line Width](#a-note-about-line-width)
- [First Layer Squish](#first-layer-squish)
- [Build Surface Adhesion](#build-surface-adhesion)
- [Pressure Advance](#pressure-advance)
    - [Tower Method (Simple)](#tower-method-simple)
    - [Marlin Method (Advanced)](#marlin-method-advanced)
    - [Fine-Tuning and What to Look For](#fine-tuning-and-what-to-look-for)
- [Extrusion Multiplier](#extrusion-multiplier)
    - [An Important Note About Pressure Advance & EM](#an-important-note-about-pressure-advance--em)
- [Cooling and Layer Times](#cooling-and-layer-times)
    - [Signs of Overheating](#signs-of-overheating)
    - [How to Fix It](#how-to-fix-it)
- [Retraction (WIP)](#retraction)
- [Miscellaneous Fixes, Tips, and Tricks](#miscellaneous-fixes-tips-and-tricks)
    - [Pinholes](#pinholes)
    - [PLA is Overheating](#pla-is-overheating)
    - [Small Infill Areas Look Overextruded](#small-infill-areas-look-overextruded)
    - [SuperSlicer Bulging Issues](#superslicer-bulging-issues)
    - [Pockmarks](#pockmarks)
    - [Repeating Patterns in Extrusion (BMG Clockwork)](#repeating-patterns-in-extrusion-bmg-clockwork)
    - [Clacking Noises During Retraction (BMG Clockwork)](#clacking-noises-during-retraction-bmg-clockwork)
    - [Belt Tooth Marks](#belt-tooth-marks)
    - [Bulges at STL Vertices](#bulges-at-stl-vertices)

# A Note About Line Width
Any line widths are expressed as a **percentage of nozzle diameter.** \
This allows the guide to remain agnostic to nozzles.

SuperSlicer natively allows percentages to be entered this way.

However: 
- Prusa Slicer bases percentages on layer heights instead.
- Cura does not allow percentages at all. 
- Other slicers may or may not support this.

**For Cura / Prusa Slicer / possibly others, you MUST use static line widths.** \
For example, enter **0.48mm** instead of **120%** if you are using a 0.4mm nozzle.


# First Layer Squish

I'm going to call it "squish" for purposes of being unambiguous. \
"z offset" and "z height" can be conflated with other concepts. \
[It stops sounding like a real word after you type it 100 times.](https://en.wikipedia.org/wiki/Semantic_satiation)

## Background and Common Issues/Mistakes

- This section assumes that you have already done a rough [Z offset calibration](https://docs.vorondesign.com/build/startup/#initial--simple-process).

- This section also assumes that you have a *consistent* first layer squish, both across the entire build surface and between prints. Here are some tips if you are having issues with either.
     - You may need to use [bed mesh](https://docs.vorondesign.com/tuning/secondary_printer_tuning.html#bed-mesh) to accomplish this. I personally recommend generating a bed mesh before every print, by adding `BED_MESH_CALIBRATE` to your `PRINT_START` macro. (requires the config section in the link above.)
        - Do not omit the `relative_reference_index` setting. This should correspond to the point you calibrate your Z offset to (almost always the center point.)
            - relative_reference_index = ((x points * y points) - 1) / 2
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
**1)** Scatter square patches around your bed in your slicer. *(See Test_Prints folder)*\
![](Images/FirstLayer-Plate.png)    

**2)** Set your first layer height to **0.25** or greater.

- Thinner first layer heights are considerably more sensitive and more difficult to maintain.

**3)** Set your first layer [line width](#a-note-about-line-width) to **120%** or greater.

**4)** Start the print. While it is printing, [live adjust z](https://docs.vorondesign.com/build/startup/#fine-tuning-z-height). Refer to the example images below.

- This can be done via g-codes/macros, LCD, or via web. I find it easiest to sit in front of the printer and fine-tune with the LCD.

**5)** Once you are happy with your squish, cancel the print and then save your new offset:

- V0/V2/Trident (dedicated Z endstop): 
    - Enter `Z_OFFSET_APPLY_ENDSTOP`. This will apply your new offset to your stepper_z's `position_endstop`.
- Switchwire/Legacy (probe used as virtual Z endstop): 
    - Enter `Z_OFFSET_APPLY_PROBE`. This will apply your new offset to your probe's `z_offset`.
- Klicky Auto z: 
    - Manually adjust your `switch_offset`. Higher value = more squish.

## Examples 
You should still clearly be able to see the lines. If it's completely smooth, your squish is too much.
 If you see gaps between the lines, you need more squish.
### Good Squish
- ![](Images/FirstLayer-PrintExample.jpg) 
### Too Much Squish

- Can't see any lines, or the lines are starting to fade:

    - ![](Images/FirstLayer-TooMuchSquish2.png) ![](Images/FirstLayer-TooMuchSquish1.png) 

- Wavy patterns appear:

    - ![](Images/FirstLayer-TooMuchSquish3.png) 


### Not Enough Squish
- There are gaps between the lines:

    - ![](Images/FirstLayer-NotEnoughSquish1.png) ![](Images/FirstLayer-NotEnoughSquish2.png) ![](Images/FirstLayer-NotEnoughSquish3.png) 


# Build Surface Adhesion


- **(!) Thoroughly wash all build plates with dish soap and water, followed by 70+% isopropyl alcohol.**

- Smooth PEI:
    - Scuff with some Scotch-Brite or a similarly rough pot scrubber or sandpaper.
    - Ensure that you actually *have* smooth PEI. Some spring steels, particularly the reverse side of some textured steels, are yellow/orange in appearance but do not actually have PEI applied. Inspect the edges of the plate to verify.

- Textured PEI:
    - Needs more squish than smooth PEI, to push the filament into the cracks/dimples.


- Avoid touching your build surface as much as possible. Oils from your fingers will cause issues. Handle your spring steel with a clean rag or cloth.

- Ensure your PEI is not counterfeit. You may have to ask in the Discord for other' experiences with a given brand. If your PEI is clear rather than yellowish, it's fake. This is particularly prevalent with random Amazon brands or unknown Aliexpress sellers.
# Pressure Advance

Pressure advance changes the **distribution** of material, not the **amount** of material.
- Lower values cause less material in the middle of lines, and more at the ends/corners. 
- Higher values cause more material in the middle of lines, and less at the ends/corners.
- Here is an example:
    - **PA Values: 0, 0.035, 0.05, 0.09, 0.12** (Direct drive - Galileo clockwork / Dragon HF)
    - ![](Images/PA-Squares.png) 


- **Remember: There is rarely such thing as perfect pressure advance.** Either accelerations or decelerations will almost always be slightly imperfect. You whould always err on the side of lower PA values.

- Pressure advance can change with different filaments. Typically I only find it necessary to tune per material type - ABS, PETG, PLA, TPU, etc.  I will only tune specific brands or colors of they are noticeably different.

There are two approaches - the [tower method](#tower-method-simple) (simple), and the [Marlin method](#marlin-method-advanced) (advanced).

## Tower Method (Simple)

This is based off of the [Klipper Pressure Advance guide](https://www.klipper3d.org/Pressure_Advance.html#tuning-pressure-advance), but with some modifications. 

The Klipper guide recommends limiting acceleration to 500 and square corner velocity (SCV) to 1, among other things. The intent behind these changes is to exaggerate the effects of pressure advance as much as possible. I'm not a fan of this approach.

In my opinion, it is best to run the calibration in close to normal printing conditions. This can make it slightly harder to tell the difference, but I find it more accurate.

**1)** Download and slice the [pressure advance tower](https://www.klipper3d.org/prints/square_tower.stl) with *your normal print settings (accelerations included)*. \
The only modifications you should make are these:

- **120mm/s** perimeter speed
- **1** perimeter
- **0%** infill
- **0** top layers
- **0 second** "minimum layer time" / "layer time goal"
- **High fan speed**

**2)** Initiate the print.

**3)** After the print has *already started\**, enter the following command:

- (Direct Drive) `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.0025`
- (Bowden) `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.025`

You should now see increasing pressure advance values reporting to the g-code terminal as the print progresses.



<sup>\* *Certain patterns in your start g-code can cancel the tuning tower. \
\* It does not matter how quickly you enter the command, as it is based on height.*\
\* Alternatively, you can temporarily add the tuning tower command after your start g-code</sup>

**4)** Allow the print to run until it starts showing obvious issues/gaps. Then you may cancel.

**5)** Measure the height of the perfect PA with calipers **(see images below)**
- Ensure you are **not** measuring your Z seam corner.
- There should be no signs of underextrusion before or after the corner. 
    - It can help to shine a bright flashlight between the walls.
- **It is normal for there to be a small amount of bulge on the trailing edge. When in doubt, choose the lower value.**
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

## Marlin Method (Advanced)

### Background
This method is quicker to run and more precise than the tower method, but requires additional preparation and manually modifying g-code files. 


**(!) If you are not familiar with manually modifying g-code, please consider using the tower method instead. You risk crashes & damage if you don't know what you are doing.**
### Method

**1)** Add this macro to your Klipper config.

```
# Convert Marlin linear advance (M900) commands to Klipper (SET_PRESSURE_ADVANCE) commands.
# Used in conjunction with Marlin's linear advance calibration tool: 
# https://marlinfw.org/tools/lin_advance/k-factor.html
[gcode_macro M900]
gcode:
	# Parameters
	{% set k = params.K|default(0)|float %}
	
	SET_PRESSURE_ADVANCE ADVANCE={k}
```

**2)** Type `RESTART` into the g-code terminal.

**3)** Visit the [Marlin K-factor calibration site](https://marlinfw.org/tools/lin_advance/k-factor.html).

**4)** Fill out the parameters. Most are self explanatory or should be left at defaults, but these are some specific settings that I recommend:
 
- **Printer**
    - **Layer Height**: 0.25mm
- **Speed**
    - **Slow Printing Speed**: Your square corner velocity
    - **Fast Printing Speed**: 120mm/sec
    - **Acceleration**: Your perimeter acceleration (NOT external perimeter)
- **Pattern**
    - **Starting Value for K**: 0
    - **Ending Value for K**:  
        - **Direct Drive**: 0.1
        - **Bowden**: 1.5
    - **K-factor Stepping:**: 
        - **Direct Drive**: 0.005
        - **Bowden**: 0.05
    - **Print Anchor Frame**: Checked
- **Advanced**
    - **Nozzle Line Ratio**: 1.2
    - **Use Bed Leveling:** No
    - **Prime Nozzle**: Unchecked
    - **Dwell Time**: 0

Note that the "Extrusion Multiplier" setting is is decimal, NOT percent.

**5)** Generate and download the g-code file.

**6)** Edit the g-code file.

**(!) Again, if you are confused about g-code editing, please consider using the tower method instead. You risk crashes & damage if you don't know what you are doing.**

I will not give extremely specific directions here, as it depends on how you start & end your prints. I will show you mine as an example, however.

- Modify the "prepare printing" g-code section appropriately at the beginning.
    - Add `PRINT_START` in the appropriate place.
        - If you are [passing variables to `PRINT_START`](https://github.com/AndrewEllis93/Ellis-PIF-Profile#passing-variables-to-print_start), remember to remove the heating commands and pass them to `PRINT_START` instead, e.g: `PRINT_START HOTEND=240 BED=110`
            - Example: \
            ![](Images/KFactor-StartGcode.png) 
    - Ensure that the preparation commands (G90, M83, G92 E0 etc.) remain, and happen **after** `PRINT_START`.

- Modify the "FINISH" g-code section appropriately at the end.
    - Don't forget to add `PRINT_END`.\
    ![](Images/KFactor-EndGcode.png) 

**7)** Print it, and inspect the results. 
- This calibration pattern is a great visual representation of what I mentioned earlier: **that there is rarely a perfect PA value.** 
    - Usually either acceleration *or* deceleration will be good, but it's rare that both will be perfect on the same line.
    - **ALWAYS** choose the lower value. In my experience this has always been the line with perfect acceleration, but imperfect deceleration.
    - This requires some interpretation. In this example, I would choose about **0.055**.

    ![](Images/KFactor-Print.jpg) 
## Fine-Tuning and What to Look For

The above methods are usually good enough on their own. Choosing the right height/line, however, can take some experience. Here are some things to look out for.
### Pressure Advance is Too High
- Divots or underextrusion at corners and line ends.
- Gaps between perimeters at corners.

- ![](Images/PA-High-1.png) 

### Pressure Advance is Too Low
- Bulging at corners and line ends.
- Gaps between straight line perimeters.

- ![](Images/PA-Low-1.png) 

You can manually tweak pressure advance based on actual prints. Usually increments of 0.005 (with direct drive) are a good starting point.

# Extrusion Multiplier

**You should [tune pressure advance](#pressure-advance) first.**\
These tests try to remove PA as a variable as much as possible, but having a good PA value is still ideal.

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
- **20-30mm/s Solid & Top Infill Speed**\
    This helps to remove pressure advance as a variable. The faster we go, the more pressure advance will impact our results. 
- **High Fan Speed**\
    As these are only small objects, we need to ensure they have enough cooling so that the top layers don't sag.

**Steps:**

**1)** Print multiple test cubes with variations of 2% EM. You can do this all in once plate by adjusting settings for each object. Save it as a .3mf file for reuse later.

**2)** Inspect each cube. Once you are nearing the correct EM, the top should feel noticeably smoother. Too much EM will look and feel rougher, and too little EM will have gaps between the lines.

**3)** If desired, run the process again but with 0.5% intervals. Most PIF providers tune down to the 0.5% range, some even less. 

I have found that most ABS falls within the 91-94% range.

### Examples

This can be difficult to convey in photos. **You may have to zoom in quite a bit to see the differences.** It's easier to see in person - especially because you can manipulate the test prints and look at them in different lighting angles.\
You will get better at this through experience.
#### 2% Intervals
![](Images/EMPrints-Coarse.png) 
#### 0.5% Intervals
Now we run the print again at 0.5% intervals between the "too low" and "too high" examples from above.

Notice how the print becomes noticeably more shiny and glass-like around perfect EM (cube #2). 
This is not just a trick of the light. Shininess is not always the best indicator, but it makes a good visual example.

![](Images/EMPrints-Fine.png) 

### An Important Note About Pressure Advance & EM
Pressure advance and flow are interrelated. The method above has you lowering your top layer speeds in order to reduce the impact of pressure advance as much as possible.

Remember: pressure advance changes the **distribution** of material, not the **amount** of material.

If your actual print results with faster top layers do not look as good as your test cubes, provided they have adequate infill, top layers, etc, **your [pressure advance](#pressure-advance) value may need further tuning.** 

You can run faster solid infill, but I would recommend using a slow-ish top surface layer still. I use 60mm/s.

### Actual Print with Tuned EM:

![](Images/EMPrint-Example.jpg) 
# Cooling and Layer Times
## Signs of Overheating
![](Images/Overheating-1.png) ![](Images/Overheating-4.png) 
![](Images/Overheating-2.png) 
![](Images/Overheating-3.png) 
![](Images/Overheating-5.png) 
![](Images/Overheating-6.png) 

## How to Fix It

People often start printing by ABS with no cooling. While this is valid advice for unenclosed printers, it's not a universal rule. **ABS often needs some cooling, especially in an enclosure.**

There are multiple things you can do to minimize overheating with ABS.

**1) Increase fan speeds.**

- The higher your chamber temperature is, the more fan speed you will need.
- Use constant fan speeds. For filaments that shrink, **varying fan speeds during a print will cause inconsistent layers and banding.** Some layers will essentially shrink more than others.
- You probably need more cooling than you think. 
    - For example I run AB-BN (5015 fan mod) and have a 63C chamber.
        - For large plates, I use 35% fan.
        - For single small objects, I use up to 80% fan.
- If your prints are curling even at low fan speeds, it may actually be a [build surface adhesion](#build-surface-adhesion) issue.
- For very large objects, you may want to be more conservative with cooling. Large objects are much more prone to warping.
    - This is the only time I might use differing fan speeds. Lower fan speeds for the majority of the print, with higher fan speeds for overhangs.

**2) Increase "minimum layer time" / "layer time goal"**

- I set this to a minimum of 15 seconds.
- This essentially slows down the print for very short/small layers, allowing each layer adequate time to cool.
- When layer times are **too short**, they do not have enough time to properly cool. You will then be printing on top of layers that are still soft.

**3) Print more objects at once, and spread them out.**

- We can allow objects to have some "break time" between layers simply by printing more objects at once. Spread them out to induce more travel time.
- ![](Images/Cooling-Spread.png) 

**4) Reduce nozzle and/or bed temperature.**

# Retraction
WIP
# Miscellaneous Fixes, Tips, and Tricks
## Pinholes

After tuning flow and pressure advance, you may still have some pinholes where your top infill meets your perimeters. This is more prevalent in PS/SS.

![](Images/Overlap-1.png) 
![](Images/Overlap-2.png) 

This is **not necessarily** an indicator that your flow or pressure advance are wrong, though they can impact it. 

Slowly increase "infill/perimeter overlap" (PS/SS) until satisfied.

Overlap Tweaked (40%):

![](Images/Overlap-Fixed1.png) 

Regarding "Not Connected" Top Infill (SuperSlicer)

- Some use "not connected" for their top infill. This does resolve the pinholes, however I find this to cause the opposite problem. It *overshoots.* 

- To resolve this overshoot, you then need to *lower* your overlap. And because overlap is a global setting, this also starts to affect sparse infill/perimeter bonding - and therefore affects print strength.


## PLA is Overheating
- Open the front door or take off all the panels. Point a fan at it.
    - Don't go too crazy, or your bed heater might not be able to keep up.

    ![](Images/Misc/PLA-Fan.png) 
- Use [AB-BN](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/Badnoob/AB-BN) or another cooling mod.
## Small Infill Areas Look Overextruded

![](Images/Misc/SmallAreas.png) 

- Some amount of this is unavoidable, but there are some things that *may* help:
    - Use single top perimeters (SuperSlicer). This simply makes these infill areas a bit larger.
    - Try reducing your pressure advance smooth time (I use 0.02)
    - Try reducing top infill speeds and accelerations.
## SuperSlicer Bulging Issues

![](Images/Misc/Bulging.png) 
![](Images/Misc/Bulging2.png) 

- Disable any "extra perimeters" and "supporting dense infill" settings.
- [Reduce perimeter accelerations considerably.](https://github.com/AndrewEllis93/Ellis-PIF-Profile#acceleration-control)

## Pockmarks

![](Images/Misc/Pockmarks.png)

- Ensure your Z seam is not set to "random".
- Dry your filament. This can be caused be moisture turning to steam and popping.
    - Extrude in midair. Watch and listen. Depending just how wet your filament is, you may hear popping noises and see steam.
## Repeating Patterns in Extrusion (BMG Clockwork)

The left cube shows this pattern. The right cube is normal.

![](Images/Misc/Backlash-Comparison.png)
![](Images/Misc/Backlash-Pattern.png)

- Test prints: https://mihaidesigns.com/pages/inconsistent-extrusion-test
- **Ensure that you have some [backlash](https://gfycat.com/mealycautiouscoqui) in your plastic gear.** You should be able to feel a small amount of "wiggle" when moving it with your fingernail (but not too much).
    - This is adjusted by moving the motor itself up and down. The motor plate has slotted screw holes to allow for adjustment.
        - You can reach the bottom left screw by opening the filament latch and inserting a ball-end hex driver.
        -  ![](Images/Misc/Backlash-Adjust.png)

    - You should have a small amount of backlash **with filament loaded and the spring tensioned.** The backlash will reduce a bit once it is loaded. You will just have to experiment.
    - This can also be caused by poor quality BMG parts. Genuine Bondtech or Trianglelab BMG parts are best.
    - Unfortunately, adjustment is not as simple for the Mini Afterburner. You will have to disassemble it and play with it. You may have to file out some screw holes to create the backlash needed. I don't have a Mini Afterburner so I can't give an exact process.

## Clacking Noises During Retraction (BMG Clockwork)
- You have *too much* backlash. See previous section.

## Belt Tooth Marks
The marks will be about 2mm apart (the same distance as the belt teeth)

![](Images/Misc/ToothMarks.png)

- Your belts may be too tight. [Your A/B belts should be about 110Hz over a 150mm length.](https://docs.vorondesign.com/tuning/secondary_printer_tuning.html#belt-tension)
    - Don't miss the video link in page linked above. 
- Your belts may be rubbing a flange somewhere.
    - It's nearly impossible to have them all running dead-center, but you can look around for belt wear and belt dust to find where it may be rubbing too much.
    - Ensure your motor pulleys are not positioned too high or too low.
    - For V2: [square your gantry](https://discord.com/channels/460117602945990666/472450547534921729/854120317299064852) and then de-rack (see below).
    - For all CoreXY printers: [de-rack.](https://www.youtube.com/watch?v=cOn6u9kXvy0)
- You may have poor quality motor pulleys and idlers.
    - I, and a few others, have had improvements from switching to authentic Gates brand pulleys and idlers. They are more expensive, but are worth it in my opinion. 
        - On v2 at least, you only need them for A/B motors and X/Y idlers. Don't waste the money on Z.
        - US source:
            - https://www.filastruder.com/products/gates-2gt-pulley?variant=15443750518855
            - https://www.filastruder.com/products/gates-2gt-idler?variant=15443755728967
    - For idlers, there is some debate over toothed vs smooth. My personal opinion is:
        - Gates toothed idlers > smooth idlers (2x F695 bearings) > china toothed idlers.

## Bulges at STL Vertices
![](Images/Misc/Vertex-Bulges.png)
- Your square corner velocity may be too low. Did you leave it set at 1 by chance?