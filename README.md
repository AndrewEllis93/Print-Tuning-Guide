# Introduction

Much of this guide is specific to Voron printers running Klipper. Rather than re-hashing concepts already described in Voron/Klipper documentation, I will be frequently linking to them and adding additional information and methods that utilize those concepts.

A handful of the [troubleshooting sections](#miscellaneous-fixes-tips-and-tricks) and some of the tuning hints focus on CoreXY (sorry, Switchwire folks).

This is not intended to be an ultimate guide to everything, rather a guide to address common mistakes and confusion I see in the Voron Discord.

**(!) Please pay special attention to anything bolded and marked with "(!)"**

My SuperSlicer profiles are located [here](https://github.com/AndrewEllis93/Ellis-PIF-Profile), along with some other information like SS tips and volumetric flow rate information with formulas.

I am adding new information all the time, be sure to check back.\
If you have issues, comments, or suggestions, please let me know on Discord: [Ellis#4980](https://discordapp.com/users/207622442842062849)

You can find bed the models and textures I am using in [Hartk's GitHub repo](https://github.com/hartk1213/MISC/tree/main/Voron%20Mods/SuperSlicer). The bed texture I am using is an older one from him in [VoronUsers.](https://github.com/VoronDesign/VoronUsers/tree/master/slicer_configurations/PrusaSlicer/hartk1213/V0/Bed_Shape) 

Thank you to **bythorsthunder** for help with testing these methods and providing some of the photos.

[![](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate?business=U6F2FZMXXSBSW&no_recurring=0&currency_code=USD)

# Table of Contents
- [Before We Begin](#-before-we-begin)
    - [**(!) Important Checks**](#-important-checks)
    - [A Note About Line Width](#a-note-about-line-width)
- [First Layer Squish](#first-layer-squish)
    - [Background and Common Issues/Mistakes](#background-and-common-issuesmistakes)
    - [Method](#method)
    - [Print Examples](#print-examples)
- [Build Surface Adhesion](#build-surface-adhesion)
- [Pressure Advance](#pressure-advance)
    - [Tower Method (Simple)](#tower-method-simple)
    - [Marlin Method (Advanced)](#marlin-method-advanced)
    - [Fine-Tuning and What to Look For](#fine-tuning-and-what-to-look-for)
- [Extrusion Multiplier](#extrusion-multiplier)
    - [Methods I'm Not a Fan Of](#methods-im-not-a-fan-of)
    - [Notes on Dimensional Accuracy](#notes-on-dimensional-accuracy)
    - [Method](#method-2)
    - [A Note About Pressure Advance & EM](#a-note-about-pressure-advance--em)
- [Cooling and Layer Times](#cooling-and-layer-times)
    - [Signs of Overheating](#signs-of-overheating)
    - [How to Fix It](#how-to-fix-it)
- [Retraction](#retraction)
- [Infill/Perimeter Overlap](#infillperimeter-overlap)
- [Troubleshooting](#troubleshooting)
    - [BMG Clockwork Backlash Issues](#bmg-clockwork-backlash-issues)
    - [Bulging](#bulging)
    - [Bulges at STL Vertices](#bulges-at-stl-vertices)
    - [PLA is Overheating](#pla-is-overheating)
    - [Pockmarks / Skips](#pockmarks--skips)
    - [Repeating Vertical Fine Artifacts (VFAs) With ~2mm Spacing](#repeating-vertical-fine-artifacts-vfas-with-2mm-spacing)
    - [Repeating Vertical Fine Artifacts (VFAs) With Non-2mm Spacing](#repeating-vertical-fine-artifacts-vfas-with-non-2mm-spacing)
    - [Small Infill Areas Look Overextruded](#small-infill-areas-look-overextruded)

# Before We Begin

## (!) Important Checks
Before you follow *any* tuning methods in this guide, ensure that:
- Your nozzle is clean.
- Your nozzle has been tightened **while hot** (unless it's a Revo), and is not leaking material through the threads around the nozzle or heatbreak.
- **(!) Your nozzle is not partially clogged.**
    - If your nozzle is partially clogged, you may not even notice.You may be able to print, but you will have an **extremely difficult time trying to tune**.
        - Ensure that you can easily extrude by hand with the filament latch open.
        - Ensure that the material falls straight down out of the nozzle when extruding midair. It should not shoot out to the side.

- Your thermistors are the correct types in your config.
    - **(!) If you use NTC100K B3950 thermistors, please see [this](https://discord.com/channels/460117602945990666/461133450636951552/896057891264561152).**
- **(!) Everything is tight (seriously, check again)**
    - Go back again and re-tighten *every single screw* you can possibly find, *especially* grub screws and everything in the toolhead. 
    - I do this once every once in a while, and I often find something that has shaken loose and is causing me issues that are *extremely* difficult to troubleshoot.
- Your motion components are clean, particularly between gear/pulley/idler teeth.

## A Note About Line Width
Any line widths are expressed as a **percentage of nozzle diameter.** \
This allows the guide to remain agnostic to nozzles.

SuperSlicer natively allows percentages to be entered this way.

However: 
- Prusa Slicer bases percentages on layer heights instead.
- Cura does not allow percentages at all. 
- Other slicers may or may not support this.

**(!) For Cura / Prusa Slicer / possibly others, you MUST use static line widths.** \
For example, enter **0.48mm** instead of **120%** if you are using a 0.4mm nozzle.

# First Layer Squish

I'm going to call it "squish" to be unambiguous. "Z offset" and "z height" can be conflated with other concepts. \
[It stops sounding like a real word after you type it 100 times.](https://en.wikipedia.org/wiki/Semantic_satiation)

## Background and Common Issues/Mistakes

- This section assumes that you have already done a rough [Z offset calibration](https://docs.vorondesign.com/build/startup/#initial--simple-process).

- This section also assumes that you have a *consistent* first layer squish, both across the entire build surface and between prints. Here are some tips if you are having issues with either.
     - You should use [bed mesh](https://docs.vorondesign.com/tuning/secondary_printer_tuning.html#bed-mesh). I personally recommend generating a bed mesh before every print, by adding `BED_MESH_CALIBRATE` to your `PRINT_START` macro. (requires the config section in the link above.)
        - Do not omit the `relative_reference_index` setting. This should correspond to the point you calibrate your Z offset to (almost always the center point.)
            - relative_reference_index = ((x points * y points) - 1) / 2
        - Some discourage using bed mesh unless absolutely necessary, but I disagree. As far as I'm concerned, it's cheap insurance. Additionally, it's rare for larger printers to have a perfect first layer without it.
        - Your heat soaked mesh will also be different from your cold mesh. It will even vary at different temperatures. This is why I prefer to generate a fresh bed mesh for every print.
        - **Bed mesh can't always save you from mechanical problems.**
            - Most bed mesh issues are caused by the gantry rather than the bed itself.
                - On V2/Trident, heat soak for 2+ hours, [square your gantry](https://discord.com/channels/460117602945990666/472450547534921729/854120317299064852) and [de-rack](https://www.youtube.com/watch?v=cOn6u9kXvy0). This helps to remove tension in your gantry, and can improve your mesh/first layer.
                    - These instructions are for V2, but the process should be similar for Trident.
                    - You have to be *somewhat* quick, as things start cooling down once you take off the panels. Don't stress about it too much though.
                - On all CoreXY printers: [de-rack](https://www.youtube.com/watch?v=cOn6u9kXvy0).
                - If you are using dual X rails, **make sure they are properly aligned with each other.** This can cause left-to-right first layer issues that mesh can't compensate for.

    - If you are using a V2: 
        - Ensure that you place your `BED_MESH_CALIBRATE` **after** G32, as G32 clears bed meshes by default.
        - Ensure that you are homing Z again after QGL, as QGL throws off Z height.

    - **(!) On larger enclosed printers (i.e. V2 & Trident), ensure that you are heat soaking for *at least* an hour.** \
    Z will drift upwards as the frame and gantry thermally expand with chamber heat. This can cause your first layer squish to vary between prints, and can even cause your first layer to drift up *as it prints*.

        Don't believe me? Look at this *(the red line)*:

         ![](/Images/ZDrift.png)

        It's not ideal, but just get into a routine - start the heat soak from your phone when you wake up in the morning.\
        There *are* ways around this - specifically by using gantry backers in combination with software-based frame thermal expansion compensation, but that is a rabbit hole well outside the scope of this guide.* 
        
        <sup>* *Some links: [1](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/whoppingpochard/extrusion_backers) [2](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/bythorsthunder/MGN9_Backers) [3](https://deepfriedhero.in/products/titanium-extrusion-backers?_pos=1&_sid=e2f989fec&_ss=r) [4](https://www.fabreeko.com/collections/voron/products/v2-4-trident-titanium-extrusion-backers) [5](https://github.com/tanaes/whopping_Voron_mods/blob/main/docs/frame_expansion/frame_thermal_compensation_howto.md) [6](https://github.com/alchemyEngine/measure_thermal_behavior) [7](https://github.com/alchemyEngine/measure_thermal_behavior/blob/main/process_frame_expansion.py) [8](https://youtu.be/RXJKdh1KZ0w)</sup>*\
        <sup>\* *This is the one thing I would ask you not to message me about. It is outside the scope of what I am hoping to accomplish with this guide. The graph above is solely intended to demonstrate my point about heat soak times.*</sup>


## Method
**1)** Scatter square patches around your bed in your slicer. *(See Test_Prints folder)*
- ![](Images/FirstLayer-Plate.png)    

**2)** Set your first layer height to **0.25** or greater.

- Thinner first layer heights are considerably more sensitive and more difficult to maintain.

**3)** Set your first layer [line width](#a-note-about-line-width) to **120%** or greater.

**4)** Start the print. While it is printing, [live adjust z](https://docs.vorondesign.com/build/startup/#fine-tuning-z-height).

- This can be done via g-codes/macros, LCD, or via web. I find it easiest to sit in front of the printer and fine-tune with the LCD.
- **Examples**\
In these examples, the third square is closest.\
There are print examples in the next section.

    - **Top surface**
        - You don't want too many ridges/hairs on top. 
            - It's normal to have a *little* bit of this near the corners, or in small footprint areas.
        - You shouldn't see any gaps between the lines.
            - It's fine to have some very small pinholes where the infill meets the perimeters.
        - ![](Images/EM-Squares-2.png)
        - ![](Images/EM-Squares-2-Annotated.png)
    - **Bottom Surface**
        - You should not have any gaps between the lines.
        - You should still be able to clearly see the lines. They should not be fading or invisible.
        - ![](Images/EM-Squares-1-Annotated.png)


**5)** Once you are happy with your squish, cancel the print and then save your new offset with one of the below methods:

- **Dedicated Z Endstop:**\
(With dedicated Z endstops. Stock V0/V2/Trident are set up this way)
    - Enter `Z_OFFSET_APPLY_ENDSTOP`* 
        - This will apply your new offset to your stepper_z's `position_endstop`.
    - Enter `SAVE_CONFIG`.

- **Virtual Z Endstop:**\
(When using the probe *as* the Z endstop. Stock Switchwire and Legacy are set up this way)
    - Enter `Z_OFFSET_APPLY_PROBE`*
        - This will apply your new offset to your probe's `z_offset`.
    - Enter `SAVE_CONFIG`.

- **Klicky Auto Z Calibration:**\
(This is a mod, it uses Klicky AND nozzle endstop to automatically baby step before each print. See [here](https://github.com/protoloft/klipper_z_calibration) for more information.)
    - Manually adjust your `switch_offset` based on how much extra you had to baby step. 
        - Higher value = more squish 
        - Lower value = less squish

<sup>* Requires a semi-recent version of Klipper.</sup>
## Print Examples 
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

- **(!)** Avoid touching your build surface as much as possible. Oils from your fingers will cause issues. Handle your spring steel with a clean rag or cloth.

- **(!) Thoroughly wash all build plates with dish soap and water, followed by 70+% isopropyl alcohol.**
    - You should do this even for brand new surfaces.
    - Isopropyl alcohol does not do a great job of cleaning oils. It mostly just spreads them around.
    - I keep a spray bottle of soapy water next to my printer. Using a paper towel, I scrub with soapy water, then again with isopropyl alcohol (IPA).
    - Soap is not needed for every print. You can use IPA most of the time, with occasional soap when it needs further refreshing.

- **Smooth PEI:**
    - **Scuff it up** with a [Scotch-Brite scouring pad](https://www.scotch-brite.com/3M/en_US/scotch-brite/tools/~/Scotch-Brite-Heavy-Duty-Scour-Pad/?N=4337+3294529207+3294631680&rt=rud).
        - The rough side of a fresh sponge, ~800-1000 grit sandpaper, or other brands of scouring pads could also work.
        - This helps immensely, much like how you would scuff/sand a surface before painting or gluing something to it.
        - You can refresh the surface this way on occasion, just remember to wash it again afterwards.
    - Ensure that you actually *have* smooth PEI. Some spring steels, particularly the reverse side of some textured steels, are yellow/orange in appearance but do not actually have PEI applied. Inspect the edges of the plate to verify.

- **Textured PEI:**
    - Needs more squish than smooth PEI, to push the filament into the cracks/dimples.

- Ensure your PEI is not counterfeit. You may have to ask in the Discord for others' experiences with a given brand. If your PEI is clear rather than yellowish, it's fake.
    - Stick to well-known brands. 
    - This is prevalent with unknown AliExpress and Amazon sellers.

- Instead of PEI, you can use strong adhesives like [Vision Miner Nano Polymer](https://visionminer.com/products/nano-polymer-adhesive) on bare spring steel.
# Pressure Advance

Pressure advance changes the **distribution** of material, not the **amount** of material.
- Lower values result in less material in the middle of lines, and more at the ends/corners. 
- Higher values result in more material in the middle of lines, and less at the ends/corners.
- Here is an example:
    - PA Values: 0, 0.035, 0.05, 0.09, 0.12 (Galileo clockwork / Dragon HF)
    - ![](Images/PA-Squares.png) 


- **Remember: There is rarely such thing as perfect pressure advance.** Either accelerations or decelerations will almost always be slightly imperfect. You should always err on the side of lower PA values.

- Pressure advance can change with different filaments. Typically I only find it necessary to tune per material type - ABS, PETG, PLA, TPU, etc.  I will only tune specific brands or colors of they are noticeably different.

There are two approaches - the [tower method](#tower-method-simple) (simple), and the [Marlin method](#marlin-method-advanced) (advanced).

## Tower Method (Simple)

This is based off of the [Klipper Pressure Advance guide](https://www.klipper3d.org/Pressure_Advance.html#tuning-pressure-advance), but with some modifications. 

The Klipper guide recommends limiting acceleration to 500 and square corner velocity (SCV) to 1, among other things. The intent behind these changes is to exaggerate the effects of pressure advance as much as possible. I'm not a fan of this approach.

In my opinion, it is best to run the calibration in close to normal printing conditions. This can make it slightly harder to tell the difference, but I find it more accurate.

**1)** Download and slice the [pressure advance tower](https://www.klipper3d.org/prints/square_tower.stl) with *your normal print settings (accelerations included)*. \
The only modifications you should make are these:

- **120mm/s** external perimeter speed
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
	{% set pa = params.K|float %}
	
	SET_PRESSURE_ADVANCE ADVANCE={pa}
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
    - Change `M204 P` to `M204 S`.
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
    - Even at the "best" PA value, the line may not be perfect thickness all the way across.
    - Often, either acceleration *or* deceleration will look good. They will not always both look good on the same line.
        - **ALWAYS** choose the lower value. 
    - This requires some interpretation. In this example, I would choose about **0.055**.\
*(note: mine may be higher than yours, I am using an Orbiter + Dragon HF.)*

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


**(!) You should [calibrate your extruder](https://docs.vorondesign.com/build/startup/#extruder-calibration-e-steps) first.**

- Calibrating your extruder ensures that the extrusion multiplier will be the same across all printers. Extruder calibration simply ensures that 100mm requested = 100mm extruded. Extrusion *multiplier* is a per-filament setting, depending on the properties of each material.

**(!) You should also [tune pressure advance](#pressure-advance) first.**

- These tests try to remove PA as a variable as much as possible, but having a good PA value is still ideal.

This must be done, at a minimum, per filament brand/type. It may vary by color or by roll, depending how consistent your filament brand of choice is. With KVP I am usually able to run the same EM for all colors.

## Background
This is a bit of a debated subject. Getting the perfect extrusion multiplier (EM) is *crucial* for good looking prints.
### Methods I'm Not a Fan Of
The below methods I've found to have error of up to 5% (sometimes even more) - which may not sound too bad but it makes a *huge* difference on the appearance of your prints.
- #### Measuring Wall Thickness With Calipers
    - Some guides you will find online mention printing a single or two-walled object and measuring the thickness with calipers. 
        - I find this method not to work very well at all, especially with ABS, presumably due to shrinkage.
        - This method is also impacted by pressure advance, which can easily throw off your results.
- #### SuperSlicer Calibration
    - SuperSlicer has a built-in flow calibration tool, however I do not like this either, for a few reasons:
        - It is very reliant on first layer squish.
        - Because it uses 100% infill, the first layer squish carries through all the way to the top. 
        - It has ironing turned on by default.
        - The objects are too small. It's normal for [smaller infill areas to look a bit more overextruded than larger infill areas.](#small-infill-areas-look-overextruded)

### Notes on Dimensional Accuracy
I find the below method to result in prints that are within my personal acceptable tolerances, and work well for Voron parts. 

Voron parts are designed both for some shrinkage, and for reasonable tolerances, so **don't go crazy with calipers and comparing measurements to CAD/STL dimensions.** 

With the Voron test prints, as long as:
- The thread tests screw together nicely, and
- Bearings fit nicely without too much force into the Voron cube (F695 on bottom, 625 on top),

Then you are pretty much good to go.

If dimensional accuracy is your top priority for other projects: 
- Firstly, adjust your expectations. Remember, our 3D printers are hobby-grade glorified hot glue guns, not CNC. You will not reliably get 0.005mm tolerances everywhere.
- The first thing I would try would be to adjust EM based on part dimensions or fitment, and use the below method to tune *top layer flow separately* for aesthetics and flush mating surfaces.
- You may also need to play with shrinkage compensation, part scaling, or CAD dimensions since we are dealing with ABS. Or you can print in a material with less shrinkage.
- There is also some debate around whether you should calibrate your A/B (or X/Y) axes. I have never found this necessary, however. 

You will have to find the method that works best for you. I am considering extremely tight dimensional accuracy outside the scope of this guide. 
## Method
By far the best method I have found is purely visual/tactile.

We will print some 30x30x3mm cubes. *(see the Test_Prints folder)*

**Print Settings:**
- **40+% Infill**\
    We need sparse infill rather than 100% solid infill, to remove the first layer squish from impacting the top layer. \
    We still need enough to adequately support the top layers.
- **120% Infill [Line Width](#a-note-about-line-width)** \
    This increases infill density if you usually run thicker infill than this.
- **100% Top Layer [Line Width](#a-note-about-line-width)**\
    This is more subject to interpretation, but I find 100% to have good results.
- **5 Top Layers**\
    This ensures that we have adequate support for the surface layer.
- **Monotonic (filled)** top infill pattern\
    Make sure that this is not set to "ironing". If not available, use rectalinear or "lines" instead (depends on slicer).
- **30mm/s Solid & Top Solid Infill Speed***\
    This helps to remove pressure advance as a variable. The faster we go, the more pressure advance will impact our results.\
    <sup>\* If your pressure advance is well tuned, you may actually get more "true to life"/accurate results printing at your normal print speeds. If your pressure advance is off, however, it will [throw you off further.](#a-note-about-pressure-advance--em)</sup>
- **High Fan Speed**\
    As these are only small objects, we need to ensure they have enough cooling so that the top layers don't sag.

**Steps:**

**1)** Print multiple test cubes with variations of 2% EM. 
- You can do this all in once plate by adjusting settings for each object. Save it as a .3mf file for reuse later.
    - **(!) In PS/SS, if you set flow per-object, make sure to set your EM to 1 in the filament settings.** The per-object EM settings are a percentage that is **multiplied by** the EM in your filament settings.
    1) ![](Images/EM-1.png)
    2) ![](Images/EM-PerObject.png)
    3) ![](Images/EM-PerObject-2.png)
    4) ![](Images/EM-PerObject-3.png)

**2)** Inspect each cube. Once you are nearing the correct EM, the top should feel noticeably smoother. Too much EM will look and feel rougher, and too little EM will have gaps between the lines.

**3)** If desired, run the process again but with 0.5% intervals. Most PIF providers tune down to the 0.5% range, some even less. 

I have found that most ABS falls within the 91-94% range.

### Examples

This can be difficult to convey in photos. **You may have to zoom in to see the differences.** It's easier to see in person - especially because you can manipulate the test prints and look at them in different lighting angles.\
You will get better at this through experience.
#### 2% Intervals
![](Images/EMPrints-Coarse.png) 
#### 0.5% Intervals
Now we run the print again at 0.5% intervals between the "too low" and "too high" examples from above.

Notice how the print becomes noticeably more shiny and glass-like around perfect EM (cube #2). 
This is not just a trick of the light. Shininess is not always the best indicator, but it makes a good visual example.

![](Images/EMPrints-Fine.png) 

### A Note About Pressure Advance & EM
Remember: pressure advance changes the **distribution** of material, not the **amount** of material.

Pressure advance and flow are interrelated, so tuning one can affect the other. The method above has you lowering your top layer speeds in order to reduce the impact of pressure advance as much as possible.

The faster you print, the larger the area that pressure advance will impact. Lower speeds will relegate the effects of pressure advance to be closer to the edges, while higher pressure advance will cause it to affect a wider area.

Imagine a single extrusion line. In this line, the toolhead accelerates to full speed, stays at top speed, and then decelerates again towards the end of the line. Pressure advance takes effect during these accelerations and decelerations. \
In both of the below examples, assume the same acceleration settings.
- When printing with a faster speed, the line is printed in less time, and the extruder spends a larger portion of the line accelerating and decelerating to reach the higher top speed. Therefore, a larger portion of the line is spent equalizing pressure.
- When printing with a slower speed, the line is printed in more time, the extruder spends a smaller portion of the line accelerating and decelerating. Therefore, a smaller portion of the line is spent equalizing pressure, and more of the line is printed at steady speed with steady pressure.

If your actual print results with faster top layers do not look as good as your test cubes, provided they have adequate infill, top layers, etc, **your [pressure advance](#pressure-advance) value may need further tuning.** 

You can run faster solid infill, but I would recommend using a moderate top layer speed still. I use 60mm/s.

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
    - For very large objects, you may want to be more conservative with cooling. Large objects are much more prone to warping.
        - This is the only time I might use differing fan speeds. Lower fan speeds for the majority of the print, with higher fan speeds for overhangs.
- If your prints are curling away from the bed even at low fan speeds, it may actually be a [build surface adhesion](#build-surface-adhesion) issue.


**2) Increase "minimum layer time" / "layer time goal"**

- I set this to a minimum of 15 seconds.
- This essentially slows down the print for very short/small layers, allowing each layer adequate time to cool.
- When layer times are **too short**, they do not have enough time to properly cool. You will then be printing on top of layers that are still soft.

**3) Print more objects at once, and spread them out.**

- We can allow objects to have some "break time" between layers simply by printing more objects at once. Spread them out to induce more travel time, and maybe even reduce travel speeds.
- ![](Images/Cooling-Spread.png) 

# Retraction

**(!) You should [tune pressure advance](#pressure-advance) first.**
Pressure advance can lower the amount of retraction needed, especially for bowden.

If you typically print with z-hop, leave it on for this test.

**There is some trial and error involved.** You may need to re-run these tests at varying retraction speeds and temperatures if you are not getting good results. You will just have to experiment. You should hot tighten your nozzle (unless it's an E3D Revo).

If you are having persistent issues:
- **(!) Ensure that your filament is dry.** Wet filament can cause near-unfixable stringing.
- Ensure that your hotend is not leaking around the threads or heat break. This can indicate that your nozzle or heatbreak is loose or not making adequate contact.

There are a few factors that can affect your retraction settings, such as:
- Material type
- Print temperature
- Hotend
- Extruder
## Method

**We will be using using [SuperSlicer](https://github.com/supermerill/SuperSlicer/releases)'s calibration tools.**

- If you do not typically use SuperSlicer, you can start with one of the built-in Voron profiles for this test. 
    - The built-in profiles are not great in my opinion, but will work fine just for running the calibration tools. 
    - Shameless plug: try [my profiles](https://github.com/AndrewEllis93/Ellis-PIF-Profile) later on. There are some other warnings and dependencies, however *(please thoroughly read its readme)*, so just stick with the built-in ones for now.

We will be printing these retraction towers at three different temperatures. If you are confident that your filament temperature is well tuned, you may get good results with just one tower.

**1)** Ensure that your nozzle is clean. You can use a brass brush while it is heated.

**2)** Set your retract and unretract speeds to **30mm/s** to start. 
- This is located in the "printer settings" tab, under "extruder 1".
- I have had more luck with slower retraction speeds. Your mileage may vary.

**3)** Use medium-high fan speeds. 
- These are located in the "filament settings" tab, under "cooling".
- These retraction towers are small and need some additional cooling. 

**4)** Select "extruder retraction calibration" from the menu.

- ![](Images/Retraction-Menu.png) 

**5)** Click "remove fil. slowdown".

- ![](Images/Retraction-FilSlowdown.png) 

**6)** Fill out the parameters and select "Generate".

- ![](Images/Retraction-Params.png) 

    - **Start temp:**
        - Set a **bit higher** than your normal printing temps.
            - For this example, I will be using 255C with KVP ABS.
    - **Step:**
        - Direct drive: **0.1mm**
        - Bowden: **0.5mm**
    - **Height:**
        - Your maximum retraction length will be **(height - 1) * step**.
            - Do not exceed **1mm** for direct drive.
                - You will *rarely* need more than this, but it is possible with some high flow hotends and setups. Start with 1mm, only go up to a max of 2mm if required.
            - For bowden, this can vary. Try starting with a maximum of **3mm**.
                - You may need more, depending on a few factors like pressure advance, bowden tube length, bowden tube internal diameter, and how firmly attached the tube is in the couplings.
                - Ensure that your bowden tubes are as firmly attached as possible, and do not [move too much in and out of their couplings during printing](https://youtu.be/lboDSH0945g?t=120). 
    - **Temp decrease (temp decr):**
        - **3x10°**.
            - This will print three retraction towers. One will be at your "start temp", the other two will be 10C increments below this.

    - You should get output like this:
        - ![](Images/Retraction-Sliced.png) 

    **7) (!) Arrange the towers front to back**\* **on your build plate.**
    - These objects are printed one at a time. **This ensures that they are not knocked over by the gantry/toolhead.** 
    - Arrange them from the hottest tower at the front, to coolest tower at the back.
        - The towers are printed from hottest to coldest. This just lowers the chance of collisions (particularly with poorly written `PRINT_END` macros)
    - ![](Images/Retraction-Sliced-FrontToBack.png)

     <sup>\* If you are using a different kinematic system than CoreXY/i3 cartesian, you may need to use a different arrangement. For example, a cross gantry would need diagonal.</sup>

    **8) Print it, and inspect the results.** 
    - If your hotter towers are much stringier, consider choosing a lower extrusion temperature.
    - **To get your new retraction length:**
        - Count the rings (from the bottom), subtract 1, and multiply by your "step" value.
            - In my opinion, choose a height **1-2 notches higher** than where the stringing disappears. This just gives you a bit more headroom for filaments that may behave a bit differently.

## Infill/Perimeter Overlap

After tuning flow and pressure advance, you may still have some pinholes where your top infill meets your perimeters. This is more prevalent in PS/SS.

This is *not necessarily* an indicator that your flow or pressure advance are wrong, though they can impact it. 

*Some people have widely varying overlap settings. You will need to tune this for yourself. I am still figuring out why it varies between people.* \
*The current theory is that it may be impacted by line width, but I have not yet tested this theory.*

**Simply increase "infill/perimeter overlap" (PS/SS) until satisfied.**

### Examples
- ![](Images/Overlap-1.png) 
- ![](Images/Overlap-2.png) 
### Overlap Tweaked:

- ![](Images/Overlap-Fixed1.png) 

### Regarding "Not Connected" Top Infill (SuperSlicer)

- Some use "not connected" for their top infill. This does resolve the pinholes, however I find this to cause the opposite problem. It *overshoots.* 

- To resolve this overshoot, you then need to *lower* your overlap. And because overlap is a global setting, this also starts to affect sparse infill/perimeter bonding - and therefore affects print strength.
# Troubleshooting

## BMG Clockwork Backlash Issues

**Ensure that you have some [backlash](https://gfycat.com/mealycautiouscoqui) between the motor gear and the plastic gear.**
- Gauge this with filament loaded and the spring tensioned (the backlash will reduce a bit once it is loaded).
- You want a little backlash, but not *too* much.

This is adjusted by moving the motor itself up and down.\
The motor plate has 3 slotted screw holes to allow for adjustment:

![](Images/Misc/Backlash-Adjust.png)

- The top two screws are easily reachable.
- The bottom left screw can be reached by opening the filament latch fully and using a ball-end hex driver.

Unfortunately, adjustment is not as simple for the Mini Afterburner. I don't have a Mini Afterburner so I can't give an exact process. You will have to disassemble it and play with it. You may have to file out some screw holes.

### Too Little Backlash:
- Repeating Patterns in Extrusion
    - Adjusting backlash can help considerably with these issues, but you are unlikely to get 100% perfect extrusion.
    - These issues can also be caused by poor quality BMG parts. Genuine Bondtech or Trianglelab BMG parts are best.
    - Test prints: https://mihaidesigns.com/pages/inconsistent-extrusion-test
    - **Examples:**
        - The left cube shows a pattern. The right cube is normal:\
    ![](Images/Misc/Backlash-Comparison.png)
        - Diagonal patterns:\
    ![](Images/Misc/Backlash-Pattern.png)
        - "Wood Grain":\
    ![](Images/Misc/Backlash-WoodGrain.png)

### Too Much Backlash:
- Clacking Noises During Retraction
## Bulging

This may or may not just be a Prusa Slicer / SuperSlicer thing. I have not tested it in other slicers. 

![](Images/Misc/Bulging.png) 
![](Images/Misc/Bulging2.png) 

- Disable any "extra perimeters" and "supporting dense infill" settings (PS/SS)
- [Reduce perimeter accelerations considerably.](https://github.com/AndrewEllis93/Ellis-PIF-Profile#acceleration-control)

## Bulges at STL Vertices
![](Images/Misc/Vertex-Bulges.png)
- Your square corner velocity may be too low. (Did you leave it set at 1 by chance?)
- This can also be a sign that your perimeter speeds/accels are too high.
## PLA is Overheating
- Open the front door or take off all the panels. Point a fan at it.
    - Don't go too crazy, or your bed heater might not be able to keep up.

    ![](Images/Misc/PLA-Fan.png) 
- Use [AB-BN](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/Badnoob/AB-BN) or another cooling mod.

## Pockmarks / Skips

![](Images/Misc/Pockmarks.png)

- Ensure your Z seam is not set to "random".
- Dry your filament. This can be caused be moisture turning to steam and popping.
    - Extrude in midair. Watch and listen. Depending just how wet your filament is, you may hear popping noises and see steam.
    - **Just because your filament was new/sealed, doesn't mean it's not wet.** I've had plenty of filaments come soaking wet even though they were sealed.
- Your extruder could be skipping. 
    - Check the volumetric speed preview in your slicer. See if it is high for [your particular hotend](https://github.com/AndrewEllis93/Ellis-PIF-Profile#approximate-values). Or see [here](https://github.com/AndrewEllis93/Ellis-PIF-Profile#determining-max-volumetric-flow-rate) to determine your maximum.
        - If you are exceeding hotend limits, try lowering your volumetric speed limit in your slicer (PS/SS) or reducing line widths / layer heights / speed (other slicers) until you are under the limit.
    - With the latch open, try extruding by hand. It should be pretty easy. If there is too much resistance, figure out where it is coming from.
        - You may need to drill out the filament path in the printed parts, sometimes they can sag.
        - Your nozzle may be partially clogged. 
            - See if extruded plastic is shooting out to the side instead of straight down when extruding in mid-air.
    - Ensure that you are using the correct `run_current` for your motor. Too high or too low can both cause skipping.
    - Check your extruder motor wiring.
## Repeating Vertical Fine Artifacts (VFAs) With ~2mm Spacing
If the marks are about 2mm apart, that usually means that it's coming from **belt/pulley/idler teeth** somewhere. 

Ensure that these artifacts are **still perfectly vertical** even when printing irregularly shaped objects like the *"rectangular 2 recommended.stl"* object [here](https://mihaidesigns.com/pages/inconsistent-extrusion-test). \
If they are not perfectly vertical (i.e. wood grain, diagonal, etc), see [this section](#repeating-patterns-in-extrusion-bmg-clockwork) instead.

Print a square object at 45 degrees and see if it appears A, B, or both. This will tell you which axis/axes to look at.

![](Images/Misc/ToothMarks.png)

- Your belts may be too tight. [Your A/B belts should be about 110Hz over a 150mm length.](https://docs.vorondesign.com/tuning/secondary_printer_tuning.html#belt-tension)
    - Don't miss the video link in page linked above. 
- Your belts may be rubbing a flange somewhere.
    - It's nearly impossible to have them all running dead-center, but you can look around for belt wear and belt dust to find where it may be rubbing too much.
    - Ensure your motor pulleys are not positioned too high or too low.
    - On V2/Trident, heat soak for 2+ hours, [square your gantry](https://discord.com/channels/460117602945990666/472450547534921729/854120317299064852) and [de-rack](https://www.youtube.com/watch?v=cOn6u9kXvy0). This helps to remove tension in your gantry, and can improve your mesh, first layer, and pulley/belt alignment.
        - These instructions are for V2, but the process should be similar for Trident.
    - On all CoreXY printers: [de-rack](https://www.youtube.com/watch?v=cOn6u9kXvy0).
- Ensure that your pulleys, idlers, and extruder gears/idlers are all clean. Debris can accumulate and compress in the teeth. 
- You may have poor quality motor pulleys and idlers.
    - I, and a few others, have had improvements from switching to authentic Gates brand pulleys and idlers. They are more expensive, but are worth it in my opinion. 
        - On v2 at least, you only need them for A/B motors and X/Y idlers. Don't waste the money on Z.
        - US source:
            - https://www.filastruder.com/products/gates-2gt-pulley?variant=15443750518855
            - https://www.filastruder.com/products/gates-2gt-idler?variant=15443755728967
    - For idlers, there is some debate over toothed vs smooth. My personal opinion is:
        - Gates toothed idlers > smooth idlers (2x F695 bearings) > china toothed idlers.
## Repeating Vertical Fine Artifacts (VFAs) With Non-2mm Spacing

Ensure that these artifacts are **still perfectly vertical** even when printing irregularly shaped objects like the *"rectangular 2 recommended.stl"* object [here](https://mihaidesigns.com/pages/inconsistent-extrusion-test). \
If they are not perfectly vertical (i.e. wood grain, diagonal, etc), see [this section](#repeating-patterns-in-extrusion-bmg-clockwork) instead.

These patterns can be subtle (lumps) or sharp like the above section's photo.

- **Ensure that your A/B pulleys and XY joint idlers are all clean.** Debris can accumulate and compress between the teeth.
- You may have a bad/poor quality pulley or toothed idler.
    - See above section for more info / links.
- You may have a bad/poor quality bearing.
    - Loosen the A/B belts, pull the belt over the side of each bearing flange, and turn each bearing by running it against your finger. Make sure the whole rotation feels smooth.
- You may have a bad/poor quality linear rail.

### Narrowing it Down
Print two square objects, one in normal orentation, and one at 45 degrees. \
Inspect the object to see which axes the artifacts appear most prominent in.

*(components in each section are in order of likelihood)*
- Artifacts are most prominent in in A:
    - Bearings in **A** belt path
    - **A** motor pulley
    - **A** belt *(rare)*
    - **A** motor *(rare)*
- Artifacts are most prominent in in B:
    - Bearings in **B** belt path
    - **B** motor pulley
    - **B** belt *(rare)*
    - **B** motor *(rare)*
- Artifacts are most prominent in in X:
    - **XY** joint idlers
    - **X** linear rails(s)
- Artifacts are most prominent in in Y:
    - **Y** linear rails
- Artifacts are most prominent in in A/B/X, but not Y:
    - **XY** joint idlers
    - **X** linear rail(s)
- Artifacts are most prominent in in A/B/Y, but not X:
    - **Y** linear rails
- Artifacts are equally prominent in all directions:
    - **A *and* B** motor pulleys
    - **X *and* Y** linear rails
    - **A *and* B** belts *(rare)*
    - **A *and* B** motors *(rare)*
## Small Infill Areas Look Overextruded

![](Images/Misc/SmallAreas.png) 

- Some amount of this is unavoidable, but there are some things that *may* help:
    - Use single top perimeters (SuperSlicer). This simply makes these infill areas a bit larger.
    - Try reducing your pressure advance smooth time (I use 0.02)
    - Try reducing top infill speeds and accelerations.