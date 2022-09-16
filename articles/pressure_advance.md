[:arrow_left: Back to Table of Contents](/README.md)

---
# Pressure Advance

**:warning: You should [:page_facing_up:calibrate your extruder](https://docs.vorondesign.com/build/startup/#extruder-calibration-e-steps) first.**

**:warning: You may have to re-tune pressure advance if you enable or disable input shaper.**

## Background

Pressure advance changes the **distribution** of material, not the **amount** of material.
- Lower values result in less material in the middle of lines, and more at the ends/corners. 
- Higher values result in more material in the middle of lines, and less at the ends/corners.
- Here is an example:
    - PA Values: 0, 0.035, 0.05, 0.09, 0.12 (Galileo clockwork / Dragon HF)
    - ![](/images/PA-Squares.png) 


- **Remember: There is rarely such thing as perfect pressure advance.** Either accelerations or decelerations will almost always be slightly imperfect. You should always err on the side of lower PA values.

- Pressure advance can change with different filaments. Typically I only find it necessary to tune per material type - ABS, PETG, PLA, TPU, etc.  I will only tune specific brands or colors if they are noticeably different.

- Pressure advance needs re-tuning when changing nozzle sizes.

There are two approaches - the  [:pushpin:lines method](/articles/pressure_advance.md#lines-method) (recommended), and the [:page_facing_up:tower method](/articles/pressure_advance_tower_method.md) (easier for newbies, but a bit less accurate).

## Lines Method

This method is quicker to run and more precise than the [:page_facing_up:tower method](/articles/pressure_advance_tower_method.md), but requires some additional setup, including some start g-code.

**:warning: If you are not willing to get familar with setting up start g-code, consider using the [:page_facing_up:tower method](/articles/pressure_advance_tower_method.md) instead.** 
- You can damage your printer if you don't set up the start g-code correctly, for example forgetting `QUAD_GANTRY_LEVEL` or `PRINT_START` (if used).

    - (You *probably* won't, but there's my disclaimer :grin:)
### Method

**1)** Visit the [:page_facing_up:pressure advance calibration site](https://realdeuce.github.io/Voron/PA/pressure_advance.html).
- Thanks to Deuce#8801 for setting this up! (It's a modified version of [:page_facing_up:Marlin's linear advance site.](https://marlinfw.org/tools/lin_advance/k-factor.html))

**2)** Fill out the parameters specific to your setup (printer name, bed size, retraction, etc.) 

**3)** Modify the **Start G-code** section.

**:warning:** *Exercise caution here. As mentioned previously, you can damage your printer if you don't set up the start g-code correctly, for example forgetting `QUAD_GANTRY_LEVEL` or `PRINT_START` (if used).*

- This is where you will set your temperatures (`M109`/`M190`).

- Copy over your slicer's start g-code (from your printer profile) and paste it beneath the `M109`/`M190`. 

    - You can usually *replace* the default contents beneath the `M109`/`M190`. There are some default preperatory g-codes (`G28`, `G32`, etc) just in case.

        - `PRINT_START` macros usually contains all of this, but please double check.

            - If you are [:page_facing_up:passing variables to `PRINT_START`](/articles/passing_slicer_variables.md), remember to append them to `PRINT_START`. Example: `PRINT_START HOTEND=240 BED=110`

                - Your variable naming may be different, e.g. `EXTRUDER=X` instead of `HOTEND=X`.

                - You can then comment out the separate heating g-codes.

            - For **Vorons** with the stock `PRINT_START` macro, this is all you need:\
            (change the temperatures appropriately, though):

                - ![](/images/pa_start_gcode.png)

    - If your start g-code has any slicer variables (for example `[first_layer_bed_temperature]`), make sure to replace them with appropriate values.

    - Remove the `M112`. This is an emergency stop, and is there as a reading comprehension check to ensure that you have verified the start g-code.

**4)** Fill out the tuning parameters. Many can be left at defaults, but here are some specific settings that I recommend:

- **Printer**
    - **Layer Height**: 0.25mm
- **Speed**
    - **Slow Printing Speed**: Your `square_corner_velocity` From your printer.cfg. Default is 5.
    - **Fast Printing Speed**: 120mm/s*
        - \* You can set this to your fastest perimeter speed to try and better simulate real life prints. However if you typically print perimeters slowly, the results may be harder to read. Faster speeds exaggerate the effect.
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

\* *The bowden values I suggest here cover a wide range of PA values (0-1.5), because each bowden setup can vary widely. Once you narrow down a general range to work in, you may want to run the test again with a narrower range of PA values.*

**5)** Generate and download the g-code file.

**6)** Print it, and inspect the results.

- Often times, the best acceleration and decelerations values will **not be on the same line.** In this case, you should pick a midpoint between both.\
\
**ALWAYS** choose the lower value if you are not entirely sure.
    - This is a great visual representation of what I mentioned earlier: **that there is rarely a perfect PA value.** 

    - In the below example, I would choose about **0.055**.\
*(note: mine is likely higher than a normal Afterburner. I am using an Orbiter + Dragon HF.)*

    - ![](/images/KFactor-Print.jpg) 

**7)** In the `[extruder]` section of your config, update `pressure_advance` to the new value and issue a `RESTART`.
- Alternatively: 
    - In **PS/SS**, you can manage this per-filament by putting `SET_PRESSURE_ADVANCE ADVANCE=<value>` in your slicer's custom filament g-code.*

        - Replace `<value>` with your desired PA.

    - In **Cura**, you can set it during slicing using [this plugin.](https://github.com/ollyfg/cura_pressure_advance_setting)

**8)** Try printing something! 
- See [:pushpin:Fine-Tuning and What to Look For](/articles/pressure_advance.md#fine-tuning-and-what-to-look-for) to get an idea of what too high/low look like with actual prints.
- Tweaking in increments of 0.005 (with direct drive) is a good starting point.

## Fine-Tuning and What to Look For

The above methods are usually good enough on their own. Choosing the right height/line, however, can take some experience. Here are some things to look out for.
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