---
layout: default
title: Extrusion Multiplier
nav_order: 5
parent: Tuning
---
{% comment %} 
# This page has moved! Please visit [the new location](https://ellis3dp.com/Print-Tuning-Guide/articles/extrusion_multiplier.html).
{% endcomment %}
# Extrusion Multiplier
{: .no_toc }

:bulb: I’m going to call it "extrusion multiplier" to be unambiguous.\
It is sometimes referred to as "flow", which can be confused with *volumetric flow rate.*

---

{: .compat}
>:dizzy: This page is compatible with all printers.

{: .prereqs}
>- You should [:page_facing_up: calibrate your extruder](./extruder_calibration.md) first.
>   - Calibrating your extruder simply ensures that 100mm requested = 100mm extruded. 
>   - Extrusion *multiplier* is a per-filament setting, depending on their material properties & tolerances.
>
>- You should [:page_facing_up: tune pressure advance](./pressure_linear_advance/introduction.md) first.

---
<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## Cura Terminology

Cura uses the term "flow" both for its extrusion multiplier *and* for its volumetric flow rate preview. They are separate concepts, however.
- Cura's version of extrusion multiplier:
    - [![](./images/extrusion_multiplier/cura_em.png)](./images/extrusion_multiplier/cura_em.png){:target="_blank"}
- Cura's flow *rate* preview - not the same thing!
    - [![](./images/extrusion_multiplier/cura_flowrate.png)](./images/extrusion_multiplier/cura_flowrate.png){:target="_blank"}

---

## Background

{: .note }
:bulb: Extrusion multiplier (EM) tuning must be done, at a minimum, per filament brand/type. It may vary by color or by spool, depending how consistent your filament brand of choice is.

Extrusion multiplier EM is a huge part of achieving good looking prints. There are some [:pushpin: tuned print examples](#tuned-print-examples) below.

Different slicers may use different flow math, and may need higher or lower EM than others.

This method uses an aesthetics-first approach. For concerns about dimensional accuracy, see the [:pushpin: Rationale & Dimensional Accuracy](#rationale--dimensional-accuracy) section.

## Method
The best method I have found is purely visual/tactile.

We will print some 30x30x3mm cubes. *(see the [:page_facing_up: test_prints folder](https://github.com/AndrewEllis93/Print-Tuning-Guide/tree/main/test_prints))*

### Print Settings
- **Infill:** 30%+ 

- **Top Layer [:page_facing_up: Line Width](./a_note_about_line_width.md):** 100%
   - **SS/PS:** ctrl+f, search: `top_infill_extrusion_width`
   - **Cura:** "Top/Bottom Line Width" - set to equal your nozzle size.
    - I anecdotally find 100% to create a nice finish and show off EM differences the best.

- **Bottom Layers:** 2
    - **SS/PS:** Also set "minimum shell thickness" to 0 **or it will override this.**
        - (Directly below, AKA `bottom_solid_min_thickness`) 
    - This just makes space for more top layers (next step).

- **Top Layers:** As many as you can fit and still have at least two layers of infill. *(About 10-11 with 0.2mm layer height)*
    - This small bit of infill helps to decouple the first layer squish. Otherwise, an over-squished first layer can propagate all the way to the top - making it appear overextruded.
    - The effects of high/low EM compound with more solid layers.
    - If using thick layers, you may want to scale the cubes up in Z.

- **Top Infill Pattern:** "Monotonic (filled)" in **PS/SS** or "Lines" in **Cura**
    - Ensure that ironing is disabled.

- **Solid Infill Speed:** Your profile's normal value
    - **Cura:** "Top/Bottom Speed"
    - It's best to tune for your actual speeds, as [:page_facing_up: flow can drop off the faster you print](./determining_max_volumetric_flow_rate.md#flow-dropoff). ("Flow Dropoff" section)

- **Top Solid Infill Speed:** Low/Moderate. 60mm/s is what I use.
    - **Cura:** "Top Surface Skin Speed"
    - Keeping this low/moderate helps with surface finish.
    - Set your print profile to the same speed you tune for here (or vice versa).

- **Minimum Layer Time:** 0
    - **SS:** "Layer Time Goal" (in filament cooling settings - AKA `slowdown_below_layer_time`)
    - **PS:** "Slow Down Print if Layer Print Time Is Below" (in filament cooling settings - AKA `slowdown_below_layer_time`)
    - **Cura:** "Minimum Layer Time"

- **Fan Speed:** Moderate to High
    - This depends on your particular setup / chamber temperatures. Maybe around 50% with a 5015 fan setup, or 80% with a 4020 fan.

### Steps

1. Slice the test cubes with variations of **1-2% EM.** 
    - **Prusa Slicer**
        - There is no way to set the EM per object. You will have to print the test objects one at a time. 

    - **SuperSlicer**
        1. **:warning: Set your EM to 1 in the filament settings.** \
        The per-object EM settings are **multiplied by** this value.\
        [![](./images/extrusion_multiplier/EM-1.png)](./images/extrusion_multiplier/EM-1.png){:target="_blank"}

        2. Import the cube STL. Right-click it and select add settings > filament.\
        [![](./images/extrusion_multiplier/EM-PerObject.png)](./images/extrusion_multiplier/EM-PerObject.png){:target="_blank"}

        3. Check "extrusion multiplier".\
        [![](./images/extrusion_multiplier/EM-PerObject-2.png)](./images/extrusion_multiplier/EM-PerObject-2.png){:target="_blank"}
        
        6. Set your EM for each test cube.\
        [![](./images/extrusion_multiplier/EM-PerObject-3.png)](./images/extrusion_multiplier/EM-PerObject-3.png){:target="_blank"}

        7. Save the project for reuse later.\
        [![](./images/extrusion_multiplier/EM-Save.png)](./images/extrusion_multiplier/EM-Save.png){:target="_blank"}
        
    - **Cura**

        1. Select each cube and enable the "flow" setting.\
        [![](./images/extrusion_multiplier/EM-PerObject-Cura.png)](./images/extrusion_multiplier/EM-PerObject-Cura.png){:target="_blank"}

        3. Set the EM on each.\
        [![](./images/extrusion_multiplier/EM-SetFlow-Cura.png)](./images/extrusion_multiplier/EM-SetFlow-Cura.png){:target="_blank"}

        4. Save the project for reuse later.\
        [![](./images/extrusion_multiplier/EM-Save-Cura.png)](./images/extrusion_multiplier/EM-Save-Cura.png){:target="_blank"}

2. Print it!

3. Inspect each cube. 
    - Near the correct EM, the top should feel noticeably smoother. Too much EM will look and feel rougher, and too little EM will have gaps or valleys between the extrusion lines.
    - See [:pushpin: examples](#examples) below.

4. If desired, run the process again but with 0.5% intervals.
    - **If you can't decide, pick the higher EM.**

## Examples
This is difficult to show in photos - you may have to zoom in. It's easier once you can manipulate and inspect them in different lighting/angles.

Focus on **:exclamation:the center:exclamation:** of the test prints. It's normal for them to look more overextruded near the edges and corners.

You will get better at this through experience.
### 2% Intervals
{: .no_toc }

Here you'll narrow down a general range to work in.

I usually start from 92% to 98%. Most filaments will fall in this range, **but not all**.

<sup>*Click the image to open. Ctrl + scroll up / down to zoom.*</sup>\
[![](./images/extrusion_multiplier/EMPrints-Coarse-Annotated.png)](./images/extrusion_multiplier/EMPrints-Coarse-Annotated.png){:target="_blank"} 

The center cube is looking pretty close.

### 0.5% Intervals
{: .no_toc }

Now you can fine-tune in 0.5% intervals.

<sup>*Click the image to open. Ctrl + scroll up / down to zoom.*</sup>\
[![](./images/extrusion_multiplier/EMPrints-Fine.png)](./images/extrusion_multiplier/EMPrints-Fine.png){:target="_blank"} 

In this example, I chose the second cube, as this particular filament started to look nice and shiny with no gapping. Your particular filament may not shine like this.


For clarity, you are **not** tuning so the lines are "just touching".\
Your infill lines should overlap a bit, and **fill the print in as much as possible without going over**.

[![](./images/extrusion_multiplier/overlap.png)](./images/extrusion_multiplier/overlap.png){:target="_blank"}

<sup>[Source](https://help.prusa3d.com/article/layers-and-perimeters_1748)</sup>

Some find magnification to help, but I don't personally find it necessary. 

### Too Low
{: .no_toc }

Holding it up with the infill lines pointing towards a light source can help. This cube's EM is too low - you can see between the lines.

[![](./images/extrusion_multiplier/em-light.png)](./images/extrusion_multiplier/em-light.png){:target="_blank"} 
### Slightly Too Low
{: .no_toc }

These cubes need a little more EM - you can see slight gapping / valleys / shadows between the lines. 

A bit too high is better than a bit too low.

[![](./images/extrusion_multiplier/EMPrints-SlightlyLow.png)](./images/extrusion_multiplier/EMPrints-SlightlyLow.png){:target="_blank"}

## Further Tips
**When assessing extrusion multiplier, *always* look at the widest areas in a given print.** 

It's fairly normal for [:page_facing_up: smaller infill areas to look a bit overextruded](./troubleshooting/small_infill_areas_overextruded.md) *(though there are a few things that can help a bit in that link- that's another topic)*

In this example, I would look at the circled area. While some of the smaller areas look overextruded, the overall EM is actually pretty good.
- [![](./images/extrusion_multiplier/em-wheretolook.png)](./images/extrusion_multiplier/em-wheretolook.png){:target="_blank"} 

## Tuned Print Examples
(ABS)
- [![](./images/extrusion_multiplier/zoom.png)](./images/extrusion_multiplier/zoom.png){:target="_blank"} 
- [![](./images/extrusion_multiplier/EMPrint-Example4.png)](./images/extrusion_multiplier/EMPrint-Example4.png){:target="_blank"} 

(eSun ABS+ - more matte)
- [![](./images/extrusion_multiplier/EMPrint-Example2.jpg)](./images/extrusion_multiplier/EMPrint-Example2.jpg){:target="_blank"} 
- [![](./images/extrusion_multiplier/EMPrint-Example3.jpg)](./images/extrusion_multiplier/EMPrint-Example3.jpg){:target="_blank"} 

---

## Rationale & Dimensional Accuracy

My above method is an **aesthetics-first approach**. This method creates very smooth top surfaces and can also help with layer consistency. The resulting prints generally have perfectly acceptable tolerances for most projects (Voron parts included) with no further compensation.

Get your prints looking great first, THEN account for dimensions if needed. (in my opinion)

### Voron Parts
- Voron parts are designed with ABS shrinkage in mind. **You do not need any compensation apart from a good EM tune.**

### If You Need True-to-CAD Dimensional Accuracy for Other Projects
- Firstly, *adjust your expectations*. 
    - Remember, our 3D printers are hobby-grade, glorified hot glue guns, not CNC. You will not reliably get 0.01mm tolerances everywhere.
- After tuning EM:
    - Try your slicer's **shrinkage compensation** settings.
        - This is pretty much glorified X/Y part scaling. 
            - Shrinkage occurs much less in the Z axis.
            - 100%-101% X/Y scaling is about the range you would expect with ABS.
        - Print any suitable test object and measure it. Ensure that you are measuring flat edges - not corner bulging or seams. Determine how much shrinkage compensation you need.
    - **Don't mess with your `steps_per_mm`/`rotation_distance`**. Deviations are almost always from material shrinkage, bulging, layer inconsistencies, etc, NOT issues with your axes. Tinkering with these values will usually only add another variable.

### Methods I'm Not a Fan Of
- **Measuring Wall Thickness With Calipers**
    - More on that [:page_facing_up: here](./misconceptions.md).

- **SuperSlicer Calibration**
    - SuperSlicer has a built-in flow calibration tool, however I do not like this either, for a few reasons:
        - It uses 100% infill, so the first layer squish carries through all the way to the top. This causes your first layer squish to impact your results.
        - It has ironing turned on by default.
        - The objects are small. It's normal for [:page_facing_up: small infill areas to look a bit more overextruded than larger infill areas.](./troubleshooting/small_infill_areas_overextruded.md)

