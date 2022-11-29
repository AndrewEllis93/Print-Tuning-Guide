[:arrow_left: Back to Table of Contents](/README.md)

---
# Pressure Advance / Linear Advance

---
This guide will call it "pressure advance", or "PA". 

"Linear advance", or "LA" is the **same thing**. 
- Marlin just calls it by a different name.
- The only difference is that Marlin's linear advance does not have a smooth time setting.

**:warning: You should [:page_facing_up:calibrate your extruder](https://docs.vorondesign.com/build/startup/#extruder-calibration-e-steps) first.**
- :fish:[:page_facing_up:Marlin instructions](https://www.3dmakerengineering.com/blogs/3d-printing/estep-calibration)

**:warning: You may have to re-tune pressure advance if you enable or disable input shaper.** 

---
# Why Pressure Advance is Needed

## What Happens Without PA

Consider an extrusion line - where the toolhead speeds up, and then slows again.\
Ideally, you would have a straight line.

In reality, however, this happens:

- ![](/images/pressure_advance/pa_graph_off.png)\
<sup>*(Source: :page_facing_up:https://marlinfw.org/assets/images/features/lin_advance/k-factor_low.png)*</sup>\
![](/images/pressure_advance/pa_off_example.png)

### Explanation
- *The numbers will refer to the image above.*

A certain pressure must be reached for plastic to flow consistently. This extrusion pressure takes a short time to build up. 

During accelerations, there will be underextrusion while the pressure has not yet built up fully **(2)**.

Then, when decelerating, that pressure will bleed off. This causes excess plastic to blob out **(4)**. It will even a little *after* deceleration has finished **(5)**.

The faster you print, the worse these effects become.

## What PA Does

Pressure advance does what the name implies - it gives an "advance of pressure" (extra pressure) for accelerations, to counter this lag.

During decelerations it does the opposite - it pulls back (kind of like an early retraction) to alleviate the built-up pressure and prevent ooze.

**Compare this image to the above image.** Notice how PA tries to cancel out those unwanted effects.

![](/images/pressure_advance/pa_graph_annotated.png)\
<sup>*(Generated using Klipper's [:page_facing_up:graph_extruder.py](https://github.com/Klipper3d/klipper/blob/master/scripts/graph_extruder.py).)*</sup>

Keep in mind that pressure advance only changes the **distribution** of material, not the **amount** of material.

## Practical Example

At lower values, you can see less material during the accelerations, and more at the decelerations (corner blobs).

At higher values, you can see more material during accelerations, and less material in the corners (corner gaps).

![](/images/pressure_advance/PA-Squares.png) 
---
# Tuning

---

:bulb: **Pressure advance will change:**
- With different filaments and brands.
    - *Different colors of the same material/brand *can* behave differently, but it's \*usually\* not significant.*
- With different nozzle sizes.
- With large hotend temperature changes.
    - *Large temp changes can affect the viscosity of the plastic (and therefore the back pressure / resistance).*
- When enabling or disabling input shaper.
- When changing hotend, extruder, or bowden tube length (NOT reverse bowden)
---

There are three approaches:
- This  [:pushpin:pattern method](/articles/pressure_advance.md#pattern-method) (recommended)
- The [:page_facing_up:tower method](/articles/pressure_advance_tower_method.md) (easier to set up for newcomers, but can be harder to read the results & less precise)
- The deprecated [:page_facing_up:"lines method"](/articles/lines_method_deprecated.md).
    - No longer recommended!
    - I created the below method specifically to address issues with the old Marlin tool!
---

## Pattern Method

**Visit [:page_facing_up:my calibration site](https://andrewellis93.github.io/pressure_advance/pressure_advance.html).**
- Fill out the form to generate the g-code and then print it. 
    - I won't go into much detail here, or this article will become 20 pages long. Treat it like a slicer.
    - Most of these settings should be relatively intuitive, or have descriptions explaining what they do. 

- You should get a result like this:
![](/images/pressure_advance/pattern.jpg)

## What You're Looking For
You are looking for the **sharpest corner** with the fewest artifacts (gaps, bulges, divots).

- *Note - **there is rarely such thing as perfect pressure advance.** You are not looking for perfection here! Just as close as you can get.*

Imagine you're holding a machinist's square over each corner.\
*(No need to ACTUALLY use a square - just an analogy.)*

In this example, I would choose around 0.04 (in green).

![](/images/pressure_advance/pattern-annotated.jpg)

I find I get the best real prints when I lean toward **higher** values. 
- For example - if your sharpest corner has a *tiny* bit of gapping, I'd still personally choose it.\
*(And then I'd just cover up the slight gapping with single top perimeters - which is unfortunately exclusive to SuperSlicer.)*

- The sharpness of these corners has a large effect on the outer surface or prints, particularly surrounding features like logos, text, slots, etc.

I personally run the test again at 0.001-0.002 intervals (with direct drive) once I have found a range to work in.

It's up to you how finely you want to tune!

---


:warning: If you can't get a clean corner, or you have gapping and bulging at the same time, **you likely have extruder issues.** 
- One thing to check is your [:page_facing_up:extruder backlash](/articles/troubleshooting/extrusion_patterns.md#extruder-backlash). This is a common cause, but only one of many!
- Make sure there is no "dead zone" when reversing extruder directions by hand.
- Make sure nothing is misaligned or loose.
- On bowden extruders, ensure that your tube fittings have minimal/no play.

It's often faster to just rebuild your extruder than to burn an entire day troubleshooting.

---

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


# Signs of Issues

The tool above should be all you need. It closely emulates real prints, and I have found little need to fine-tune afterwards.

Still, it's good to know what to look out for:

## Pressure Advance is Too High
- Divots or underextrusion at corners and line ends.
- Gaps between perimeters at corners.
- ![](/images/pressure_advance/PA-High-1.png) 

## Pressure Advance is Too Low
- Bulging at corners and line ends.
- Gaps between straight line perimeters.
- ![](/images/pressure_advance/PA-Low-1.png) 

---

[:arrow_left: Back to Table of Contents](/README.md)