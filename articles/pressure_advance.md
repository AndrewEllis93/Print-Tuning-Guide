[:arrow_left: Back to Table of Contents](/README.md)

---
# Pressure Advance

**:warning: You should [:page_facing_up:calibrate your extruder](https://docs.vorondesign.com/build/startup/#extruder-calibration-e-steps) first.**

**:warning: You may have to re-tune pressure advance if you enable or disable input shaper.** 

:first_quarter_moon: If you are using Marlin, this page is still relevant, but: 
- You will use [:page_facing_up:Marlin's calibration site](https://marlinfw.org/tools/lin_advance/k-factor.html) instead. 
- Marlin's version is called "linear advance", but the concepts are the same.
- Linear advance does not have smoothing.
## Why PA is Needed

### Without PA
![](/images/pa_graph_off.png)\
<sup>*(Source: :page_facing_up:https://marlinfw.org/assets/images/features/lin_advance/k-factor_low.png)*</sup>\
<sup>*You can see the real-world version of this [:pushpin:below](/articles/pressure_advance.md#result). (The bottom line has PA completely off.)*</sup>

A certain pressure must be reached to achieve the expected flow rate. This extrusion pressure takes a short time to build up. During accelerations, there will be underextrusion while the pressure is still building up. **(2)**.

Inversely, when decelerating, that pressure will bleed off. This causes excess plastic to release during deceleration **(4)** and even after deceleration has finished **(5)** while the pressure bleeds off. This causes bulging/blobbing/oozing (often in corners).

The faster you print, the worse these effects become.

## What PA Does

Pressure advance does what the name implies - it gives an "advance of pressure" (extra pressure) for accelerations, to counter this lag.\
During decelerations it does the opposite - it pulls back (kind of like an early retraction) to alleviate the built-up pressure and prevent ooze.

**Compare this image to the above image.** Notice how PA tries to cancel out those unwanted effects.

![](/images/pa_graph_annotated.png)\
<sup>*(Generated using Klipper's [:page_facing_up:graph_extruder.py](https://github.com/Klipper3d/klipper/blob/master/scripts/graph_extruder.py).)*</sup>

Keep in mind that pressure advance only changes the **distribution** of material, not the **amount** of material.

## Practical Example

Here is a practical example. The perimeters were printed counter-clockwise.
- The PA values increase from left to right. 
    - PA Values: 0, 0.035, 0.05, 0.09, 0.12 (Galileo clockwork / Dragon HF)
- At lower values, you can see less material during the accelerations, and more at the decelerations (corner blobs).
- At higher values, you can see more material during accelerations, and less material in the corners (corner gaps).

![](/images/PA-Squares.png) 

## Tuning

**There is rarely such thing as perfect pressure advance.** Either accelerations or decelerations will almost always be slightly imperfect. You should always err on the side of lower PA values.

- Pressure advance can change with different filaments. Typically I only find it necessary to tune per material type - ABS, PETG, PLA, TPU, etc.  I will only tune specific brands or colors if they are noticeably different.
- Pressure advance needs re-tuning when changing nozzle sizes.

There are two approaches - the  [:pushpin:lines method](/articles/pressure_advance.md#lines-method) (recommended), and the [:page_facing_up:tower method](/articles/pressure_advance_tower_method.md) (easier for newbies, but a bit less accurate).

## Lines Method

This method is quicker to run and more precise than the [:page_facing_up:tower method](/articles/pressure_advance_tower_method.md), but requires some additional setup, including some start g-code.

**:warning: If you are not willing to get familar with setting up start g-code, consider using the [:page_facing_up:tower method](/articles/pressure_advance_tower_method.md) instead.** 
- You can damage your printer if you don't set up the start g-code correctly, for example forgetting `QUAD_GANTRY_LEVEL` or `PRINT_START` (if used).
    - (You *probably* won't, but there's my disclaimer :grin:)
### Steps

**1)** Visit the [:page_facing_up:pressure advance calibration site](https://realdeuce.github.io/Voron/PA/pressure_advance.html).
- Thanks to Deuce#8801 for setting this up! (It's a modified version of [:page_facing_up:Marlin's linear advance site.](https://marlinfw.org/tools/lin_advance/k-factor.html))

**2)** Fill out the parameters specific to your setup (printer name, bed size, retraction, etc.) 

**3)** Modify the **Start G-code** section.

**:warning:** *Exercise caution here. As mentioned previously, you can damage your printer if you don't set up the start g-code correctly, for example forgetting `QUAD_GANTRY_LEVEL` or `PRINT_START` (if used).*
- This is where you will set your temperatures (`M109`/`M190`).
- Copy over your slicer's start g-code (from your printer profile) and paste it beneath the `M109`/`M190`. 
    - You can usually replace the default gcode beneath the `M109`/`M190` with your own start g-code*, but use your best judgment. The defaults are there as safeguards.
        - Stock `PRINT_START` macros usually contain all the necessary start gcode (minus the temperatures), but please double check.
            - For **Vorons** with the stock `PRINT_START` macro, this is all you need:
                - ![](/images/pa_start_gcode.png)
            - If you are [:page_facing_up:passing variables to `PRINT_START`](/articles/passing_slicer_variables.md), remember to append them here. Example: `PRINT_START HOTEND=240 BED=110`
                - Your variable naming may be different, e.g. `EXTRUDER=X` instead of `HOTEND=X`.
                - You can then comment out the separate heating g-codes.
    - Remove the `M112`. This is an emergency stop / reading comprehension check to ensure you have reviewed the start gcode.
    - \* *If the start g-code from your slicer has any slicer variables (for example `[first_layer_bed_temperature]`), make sure to replace them with appropriate values.*


**4)** Fill out the tuning parameters. Many can be left at defaults, but here are some specific settings that I recommend:
- **Printer**
    - **Layer Height**: 0.25mm
- **Speed**
    - **Slow Printing Speed**: Your `square_corner_velocity` From your printer.cfg. Default is 5.
    - **Fast Printing Speed**: Your fastest perimeter speed*
        - \* If your perimeter speeds are particularly slow, it may be hard to read the results. You may need to use a higher speed here in that case.
    - **Acceleration**: Your perimeter acceleration
- **Pattern**
    - **Starting Value for PA:** 0
    - **Ending Value for PA:**
        - **Direct Drive:** 0.1
        - **Bowden:** 1.5*
    - **PA Stepping:**
        - **Direct Drive:** 0.005
        - **Bowden:** 0.05*
    - **Test Line Spacing:**
        - **Voron 0 (120mm bed):** 4
        - **Default**: 5
    - **Print Anchor Frame**: Checked
- **Advanced**
    - **Nozzle Line Ratio**: 1.2
    - **Prime Nozzle**: Unchecked
    - **Dwell Time**: 0

\* *These bowden values cover a wide range of PA (0-1.5), because each bowden setup can vary widely. Once you narrow down a general range to work in, you may want to run the test again with a narrower range of PA values.*

**5)** Generate and download the g-code file.

**6)** Print it, and inspect the results.

- In the below example, I would choose about **0.055**.
    #### Result
- ![](/images/KFactor-Print.jpg) 
- Sometimes the best acceleration and decelerations values will not be on the same line. In this case, you should pick a midpoint between both.
    - If they are more than a line or two apart:
        - This often happens when there's too much [:page_facing_up:backlash](https://gfycat.com/mealycautiouscoqui) in the extruder. Pressure advance uses a reverse extruder move during decelerations. Excessive backlash causes some of that reverse move to be lost. 
        - You still want a tiny amount of backlash (when filament is loaded) to ensure your extruder gears aren't over tensioned.
- Always choose the lower value if you are not entirely sure.
- This is a great visual representation of what I mentioned earlier: **that there is rarely a perfect PA value.** 

**7)** In the `[extruder]` section of your config, update `pressure_advance` to the new value and issue a `RESTART`.
- Alternatively: 
    - In **PS/SS**, you can manage this per-filament by putting `SET_PRESSURE_ADVANCE ADVANCE=`\<value> in your custom filament g-code.
        - You can also set different values for different nozzle sizes using [:page_facing_up:this](https://github.com/AndrewEllis93/Ellis-PIF-Profile#changing-pa-based-on-nozzle-size).
    - In **Cura**, you can set it during slicing using [:page_facing_up:this plugin.](https://github.com/ollyfg/cura_pressure_advance_setting)

**8)** Try printing something! 

## Fine-Tuning and What to Look For

The above method is usually pretty close on its own, but here are some things to look out for.

### Pressure Advance is Too High
- Divots or underextrusion at corners and line ends.
- Gaps between perimeters at corners.
- ![](/images/PA-High-1.png) 

### Pressure Advance is Too Low
- Bulging at corners and line ends.
- Gaps between straight line perimeters.
- ![](/images/PA-Low-1.png) 

---

[:arrow_left: Back to Table of Contents](/README.md)