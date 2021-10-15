# Introduction

Much of this guide is specific to Voron printers running Klipper. Rather than re-hashing concepts already described in Voron documentation, I will be frequently linking to it and adding additional information and methods that utilize those concepts.

Slicer screenshots are be taken in SuperSlicer, but any concepts should directly translate to any slicer of your choosing.
# Table of Contents
- [Extrusion Multiplier (Flow %)](#extrusion-multiplier-flow-)
- [First Layer Squish](#first-layer-squish)
- [Pressure Advance](#pressure-advance)

# Extrusion Multiplier (Flow %)

![](Images/EM.png)  

## Background


This is a widely misunderstood and debated subject. Getting the perfect extrusion multiplier (EM) is *crucial* for good looking prints.

Some guides you will find online mention printing a single or two-walled object and measuring the thickness with calipers. I find this method not to work very well at all, especially with ABS, presumably due to shrinkage.

SuperSlicer has a built-in flow calibration tool, however I do not like this either, for a few reasons:
- It is very reliant on first layer squish.
- Because it uses 100% infill, the first layer squish carries through all the way to the top. 
- It has ironing turned on by default.
- The objects are too small. It's normal for smaller infill areas to look a bit more overextruded than larger infill areas.

Both of the above methods I've found to have error of up to 5% (sometimes even more) - which may not sound too bad but it makes a *huge* difference on the appearance of your prints.

## Method
By far the best method I have found is purely visual. *Put the calipers down for now*.

We will print some 30x30x3mm cubes. <i>(see the Test_Prints folder)</i>

<b>Print Settings:</b>
- <b>40+% Infill</b>\
    We need sparse infill rather than 100% solid infill, to remove the first layer squish from impacting the top layer. 
    We still need enough to adequately support the top layers.</i>
- <b>120% Infill Line Width</b>\
    This just increases infill density over my normal settings, which are thicker for reducing print times.
- <b>100% Top Layer Line Width</b>\
    This is more subject to interpretation, but I find 100% to have good results.
- <b>5 Top Layers</b>\
    This ensures that we have adequate support for the surface layer.
- <b>20-30mm/s Top Layer Speed</b>\
    This helps to remove pressure advance as a variable. The faster we go, the more pressure advance will impact our results.
- <b>0.03 Pressure Advance</b> (only if you have not yet tuned it)\
    This is simply a PA value on the lowest end of the normal range. 

<b>Steps:</b>

<b>1)</b> Print multiple test cubes with variations of 2% EM. You can do this all in once plate by adjusting settings for each object. Save it as a .3mf file for reuse later.

<b>2)</b> Inspect each cube. Once you are nearing the correct EM, the top should feel noticeably smoother. Too much EM will look and feel rougher, and too little EM will have gaps between the lines.

<b>3)</b> If desired, run the process again but with 0.5% intervals. Most PIF providers tune down to the 0.5% range, some even less. 

I have found that most ABS falls within the 91-94% range.

This image shows 0.5% intervals. Notice how the print becomes noticeably more shiny and glass-like around perfect EM (cube #3). This is not just a trick of the light. Shininess is not always the best indicator, but it makes a good visual example.

![](Images/EMPrints-Fine.png) 

Example of an actual print with tuned EM:

![](Images/EMPrint-Example.jpg) 

# First Layer Squish

## Background and Common Mistakes

- This section assumes that you have already done a rough [Z offset calibration](https://docs.vorondesign.com/build/startup/#initial--simple-process).

- This section also assumes that you have a <i>consistent</i> first layer.
     - You may need to use [bed mesh](https://docs.vorondesign.com/tuning/secondary_printer_tuning.html#bed-mesh) to accomplish this. I personally recommend generating a bed mesh before every print by adding `BED_MESH_CALIBRATE` to your `PRINT_START` (after adding the relevant config section). \
     Some discourage using bed mesh unless absolutely necessary, but I disagree. As far as I'm concerned, it's cheap insurance. 

    - If you are using a V2: 
        - Ensure that you place your `BED_MESH_CALIBRATE` <b>after</b> G32, as G32 clears bed meshes by default.
        - Ensure that you are homing Z again after QGL, as QGL throws off Z height.

    - If you are having trouble getting consistent first layers and squish, <i>particularly on enclosed large printers</i>, ensure that you are heat soaking your printer for at least 45 minutes. Z will drift upwards as the frame and gantry thermally expand with chamber heat.



## Method
<b>1)</b> Scatter square patches around your bed in your slicer. <i>(See Test_Prints folder)</i>

![](Images/FirstLayer-Plate.png)    

<b>2)</b> Set your first layer height to <b>0.25</b> or greater.\
    - Thinner first layer heights are considerably more sensitive and more difficult to maintain.

<b>3)</b> Start the print. While the print is happening, [live adjust z](https://docs.vorondesign.com/build/startup/#fine-tuning-z-height). Refer to the example images below.\
    - This can be done via macros, LCD, or via web. I find it easiest to sit in front of the printer and fine-tune with the LCD.\

<b>4)</b> Once you are happy with your squish, cancel the print and then save your new offset by entering `Z_OFFSET_APPLY_ENDSTOP`. This will apply your new offset to your Z `position_endstop` in your config.\
    - If you are using the probe as a virtual endstop (rare), you would instead issue `Z_OFFSET_APPLY_PROBE`.\
    - If you are using Klicky auto z calibration, you will have to manually adjust your `switch_offset` accordingly. Higher `switch_offset` = more squish.

<b>Examples:</b>

![](Images/FirstLayerPrint-Example.jpg) 

# Pressure Advance

## Background
## Method