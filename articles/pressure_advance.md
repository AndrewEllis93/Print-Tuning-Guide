[:arrow_left: Back to Table of Contents](/README.md)

---
# Pressure Advance

**:warning: You should [:page_facing_up:calibrate your extruder](https://docs.vorondesign.com/build/startup/#extruder-calibration-e-steps) first.**
- :fish:[:page_facing_up:Marlin instructions](https://www.3dmakerengineering.com/blogs/3d-printing/estep-calibration)

**:warning: You may have to re-tune pressure advance if you enable or disable input shaper.** 
- (I personally haven't really found this to be the case, but that's what the Klipper docs say)

:fish: If you are using Marlin, this page is still relevant, but: 
- Marlin's version is called "linear advance" rather than "pressure advance", but the concepts are exactly the same.
- Marlin's linear advance does not have smoothing.
## Why PA is Needed

### Without PA
![](/images/pressure_advance/pa_graph_off.png)\
<sup>*(Source: :page_facing_up:https://marlinfw.org/assets/images/features/lin_advance/k-factor_low.png)*</sup>\
![](/images/pressure_advance/pa_off_example.png)

A certain pressure must be reached to achieve the expected flow rate. This extrusion pressure takes a short time to build up. During accelerations, there will be underextrusion while the pressure is still building up. **(2)**.

Inversely, when decelerating, that pressure will bleed off. This causes excess plastic to release during deceleration **(4)** and even after deceleration has finished **(5)** while the pressure bleeds off. This causes bulging/blobbing/oozing (often in corners).

The faster you print, the worse these effects become.

## What PA Does

Pressure advance does what the name implies - it gives an "advance of pressure" (extra pressure) for accelerations, to counter this lag.\
During decelerations it does the opposite - it pulls back (kind of like an early retraction) to alleviate the built-up pressure and prevent ooze.

**Compare this image to the above image.** Notice how PA tries to cancel out those unwanted effects.

![](/images/pressure_advance/pa_graph_annotated.png)\
<sup>*(Generated using Klipper's [:page_facing_up:graph_extruder.py](https://github.com/Klipper3d/klipper/blob/master/scripts/graph_extruder.py).)*</sup>

Keep in mind that pressure advance only changes the **distribution** of material, not the **amount** of material.

## Practical Example

Here is a practical example. The perimeters were printed counter-clockwise.
- The PA values increase from left to right. 
    - PA Values: 0, 0.035, 0.05, 0.09, 0.12 (Galileo clockwork / Dragon HF)
- At lower values, you can see less material during the accelerations, and more at the decelerations (corner blobs).
- At higher values, you can see more material during accelerations, and less material in the corners (corner gaps).

![](/images/pressure_advance/PA-Squares.png) 

## Tuning

**There is rarely such thing as perfect pressure advance.** Either accelerations or decelerations will almost always be slightly imperfect.

- Pressure advance can change with different filaments. Typically I only find it necessary to tune per material type - ABS, PETG, PLA, TPU, etc.  I will only tune specific brands or colors if they are noticeably different.
- Pressure advance needs re-tuning when changing nozzle sizes.

There are three approaches. This  [:pushpin:pattern method](/articles/pressure_advance.md#pattern-method) (recommended), the [:page_facing_up:tower method](/articles/pressure_advance_tower_method.md) (easier to set up for newcomers, but can be a bit harder to read the results), and the deprecated [:page_facing_up:"lines method"](/articles/lines_method_deprecated.md) (no longer recommended).

## Pattern Method
### :warning: The previous "lines method" has been deprecated!
### The new tool can be found [:page_facing_up:here](https://andrewellis93.github.io/pressure_advance/pressure_advance.html). 
<sup>*If it's not displaying correctly, clear your browser cache or use incognito mode.*</sup>

- I created this new version specifically to address the shortcomings of the "lines method".
- This document will be updated soon with more detailed instructions! 
    - The new tool should hopefully be pretty intuitive on its own, however. Try it out!
        - :bulb: Quick tip:
            - With this new tool, it's generally better to err on the *higher* side, unlike with the lines method.
            - I found that choosing a PA value right before corner gapping starts resulted in the best real-world prints.

- ~~Marlin support will be added soon.~~ Marlin is now supported!

<sup>*The old method can still be found [:page_facing_up:here](/articles/lines_method_deprecated.md) if you prefer it, but I'd highly recommend using this new tool instead.*</sup>

## Saving Your Pressure Advance Value
In the `[extruder]` section of your config, update `pressure_advance` to the new value and issue a `RESTART`.
- Alternatively: 
    - In **PS/SS**, you can manage this per-filament by putting `SET_PRESSURE_ADVANCE ADVANCE=`\<value> in your custom filament g-code.
        - You can also set different values for different nozzle sizes using [:page_facing_up:this](https://github.com/AndrewEllis93/Ellis-SuperSlicer-Profiles#changing-pa-based-on-nozzle-size).
    - In **Cura**, you can set it during slicing using [:page_facing_up:this plugin.](https://github.com/ollyfg/cura_pressure_advance_setting)
- **:fish:Marlin:**
    - Place `M900 K`\<value\> in your filament g-code (same as above). This must be set each time.
    - You can save a permanent default to the firmware by modifying Configuration_adv.h and reflashing the firmware. Instructions in the "Saving the K-Factor in the Firmware" section [:page_facing_up:here](https://marlinfw.org/docs/features/lin_advance.html).
    - In **Cura**, you can set it during slicing using [:page_facing_up:this plugin.](https://github.com/fieldOfView/Cura-LinearAdvanceSettingPlugin)

## Fine-Tuning and What to Look For

The above method is usually pretty close on its own, but here are some things to look out for.

### Pressure Advance is Too High
- Divots or underextrusion at corners and line ends.
- Gaps between perimeters at corners.
- ![](/images/pressure_advance/PA-High-1.png) 

### Pressure Advance is Too Low
- Bulging at corners and line ends.
- Gaps between straight line perimeters.
- ![](/images/pressure_advance/PA-Low-1.png) 

---

[:arrow_left: Back to Table of Contents](/README.md)