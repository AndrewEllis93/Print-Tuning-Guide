[:arrow_left: Back to Table of Contents](/README.md)
# Extrusion Multiplier

**:warning: You should [:page_facing_up:calibrate your extruder](https://docs.vorondesign.com/build/startup/#extruder-calibration-e-steps) first.**

- Calibrating your extruder ensures that the extrusion multiplier will be the same across all printers. Extruder calibration simply ensures that 100mm requested = 100mm extruded. Extrusion *multiplier* is a per-filament setting, depending on the properties of each material.

**:warning: You should [:page_facing_up:tune pressure advance](/articles/pressure_advance.md) first.**


This must be done, at a minimum, per filament brand/type. It may vary by color or by roll, depending how consistent your filament brand of choice is. With KVP I am usually able to run the same EM for all colors.

Some Slicers seem to "like" slightly higher or lower EM than others.

## Background

Getting the perfect extrusion multiplier (EM) is *crucial* for good looking prints.

**If you want to skip past my rambling, click [:pushpin:here](/articles/extrusion_multiplier.md#method) to go straight to the instructions.**

This is a debated subject, but I will try to explain my rationale.
### Methods I'm Not a Fan Of
- #### Measuring Wall Thickness With Calipers
    - Some guides you will find online mention printing a single or two-walled object and measuring the thickness with calipers.
        - I simply never have good results with this approach, and different people seem to get (sometimes wildly) different results.

        - The measured widths can vary depending where you measure it and how much pressure you use.

        - Any layer wobble whatsoever (which all printers have, in varying degrees) causes these walls to measure thicker, which can throw things off.

        - This method assumes that you have good calipers, which many people don't. This can simply limit the accessibility.
- #### SuperSlicer Calibration
    - SuperSlicer has a built-in flow calibration tool, however I do not like this either, for a few reasons:

        - Because it uses 100% infill, the first layer squish carries through all the way to the top. This causes your first layer squish to impact your results.

        - It has ironing turned on by default, which is an odd choice.

        - The objects are too small. It's normal for [:page_facing_up:smaller infill areas to look a bit more overextruded than larger infill areas.](/articles/troubleshooting/small_infill_areas_overextruded.md)

### Get your prints as smooth as a baby's bottom, THEN account for dimensions if needed.

(in my opinion)

My below method is an **aesthetics-first approach**. This method creates very smooth top surfaces, and additionally can help with layer consistency.

This also results in prints that are of perfectly acceptable tolerances for Voron parts (and most other projects) with no further compensation. 

**:warning: Voron parts are designed with shrinkage in mind, so it's fine if the dimensions don't perfectly match CAD.** Please don't drive yourself crazy with calipers for Voron parts, they are not always intended to match.

- With the Voron test prints, you are good to go as long as:

    - The thread tests screw together nicely, and

    - Bearings fit nicely without too much force into the Voron cube (F695 on bottom, 625 on top).
### If you need true-to-CAD dimensional accuracy for other projects
- Firstly, *adjust your expectations*. 

    - Remember, our 3D printers are hobby-grade, glorified hot glue guns, not CNC. You will not reliably get 0.01mm tolerances everywhere.

- AFTER tuning extrusion multiplier using my below method:

    - Try your slicer's **shrinkage compensation** settings.

        - In some slicers, this is just re-named/glorified X/Y part scaling*. 
            - \*Shrinkage occurs much less in the Z axis.
            - 100.5%-101% X/Y scaling is about the range you would expect with ABS.
        - Find any suitable test object (larger is generally better), and ensure that you are measuring flat edges and not any corner bulging or seams. Use the resulting measurements to determine how much shrinkage compensation you need.
    - Don't mess with your X/Y/A/B `steps_per_mm`/`rotation_distance`, you will just further confuse matters. You are almost always seeing material shrinkage, bulging, layer inconsistencies, etc, NOT issues with your axes. 
        - If dimensions are off by large amounts, you may have the wrong pulleys installed on your motors (for example if you're off by 20%, you probably swapped a 16t pulley with a 20t pulley or vice versa).

## Method
The best method I have found is purely visual/tactile.

We will print some 30x30x3mm cubes. *(see the [:page_facing_up:test_prints folder](/test_prints))*

**Print Settings:**
- **Infill:** 40%+

    - Some sparse infill helps to remove first layer squish from impacting the top layer. 

    - To adequately support the top layers so they don't sag.

- **Top Layer [:page_facing_up:Line Width](/articles/a_note_about_line_width.md):** 100%

   - SS/PS: ctrl+f, search: `top_infill_extrusion_width`

   - Cura: "Top/Bottom Line Width" - set to equal your nozzle size

    - This is more subject to interpretation, but I find 100% to have good results. It has a nice finish and tends to show off EM differences the best.

- **Bottom Layers:** 2
    - SS/PS: Make sure "minimum shell thickness" is disabled (directly below) - it will override this.

    - This makes more space for top layers. See "top layers" details below.

- **Top Layers:** As many as you can fit and still have at least two layers of infill.\
(about 12 with 0.2mm layer height)

    - The 2 layers of infill provides a small void for any first layer squish issues to settle. Otherwise, an over-squished first layer could carry all the way through to the top surface.

    - **The more solid layers we print, the more underextrusion or overextrusion will show**. The effects compound (well, up to a point).

        - If you are printing with especially thick layer heights, you can scale the cubes up in Z a bit to ensure that you have enough solid layers.

- **Top Infill Pattern:** Monotonic (filled)

    - Cura: "Top/Bottom Pattern" - set to "lines"

    - Make sure that this is not set to "ironing". If not available, use rectalinear or "lines" instead (depends on slicer).

- **Solid Infill Speed:** Your Profile's Normal Value

    - Cura: "Top/Bottom Speed"

    - It's best to tune for your normal speeds, as flow can [:page_facing_up:drop off a little bit the faster you print](/articles/determining_max_volumetric_flow_rate.md#theory-vs-reality) ("Theory vs Reality" section)

- **Top Solid Infill Speed:** 60mm/s Max
    - Cura: "Top Surface Skin Speed"

    - I recommend printing your very top layer quite slowly, both for the tests and for your regular prints. It can result in nicer top surfaces.

        - Set your regular printing profile to match.

    - If you *must* go faster in your normal printing profile, use your normal speed here instead.

- **Fan Speed:** High

    - As these are only small objects, we need to ensure they have enough cooling so that they don't get melty or sag. 
    
    - This depends on your fan and chamber temperatures, maybe around 80% with a 5015 fan setup, or 100% with a 4020 fan.

**Steps:**

**1)** Set up your slicer with test cubes with variations of **1-2% EM.** 
- You can do this all in once plate by adjusting settings for each object. Save it as a .3mf file for reuse later.
    - **Prusa Slicer:**
        - There is no way to set the EM per object. You will have to print the test objects one at a time. 

    - **SuperSlicer:**
        1) **:warning: Make sure to set your EM to 1 in the filament settings.** \
        The per-object EM settings are a percentage that is **multiplied by** the EM in your filament settings.\
        ![](/images/EM-1.png)

        2) Import the cube STL. Right-click it and select add settings > filament.\
        ![](/images/EM-PerObject.png)

        3) Check "extrusion multiplier".\
        ![](/images/EM-PerObject-2.png)
        
        4) Right-click the cube in the pane on the right, and select "set number of instances". In the prompt, enter your desired number of cubes.\
        ![](/images/EM-Instances.png)

        5) Select the first instance, hold shift, and then click the last instance (to select all of them). Right click and select "set as separated objects".\
        ![](/images/EM-SeparateObjects.png)

        6) This will automatically add the custom setting to all of your test cubes! Now go through each object and set an extrusion multiplier for each.\
        ![](/images/EM-PerObject-3.png)

        7) Save the project for reuse later.\
        ![](/images/EM-Save.png)
        
    - **Cura:**

        1) Import the STL. Select it, and then and enable the per-object "flow" setting for it.\
        ![](/images/EM-PerObject-Cura.png)

        2) Right-click the cube and select "multiply selected". Enter your desired number of test cubes in the prompt.\
        ![](/images/EM-Instances-Cura.png)

        3) Click on each cube and set the EM on each. The setting should already be exposed on each object since we multiplied it.\
        ![](/images/EM-SetFlow-Cura.png)

        4) Save the project for reuse later.\
        ![](/images/EM-Save-Cura.png)

**2)** Print it!

**3)** Inspect each cube. Once you are nearing the correct EM, the top should feel noticeably smoother. Too much EM will look and feel rougher, and too little EM will have gaps between the lines.

**4)** If desired, run the process again but with 0.5% intervals. Most PIF providers tune down to the 0.5% range, some even less. 

I have found that most ABS falls within the 91-94% range.

## Examples

This can be difficult to convey in photos. **You may have to zoom in to see the differences.** It's easier to see in person - especially because you can manipulate the test prints and look at them in different lighting angles.

Also note that some filaments show EM differences more than others. 

Focus all of your attention **:exclamation:at the center:exclamation:** of the test prints. It's normal for it to look a bit more overextruded near the edges and corners.

You will get better at this through experience.
### 2% Intervals
![](/images/EMPrints-Coarse-Annotated.png) 
### 0.5% Intervals
Now we run the print again at 0.5% intervals between the "too low" and "too high" examples from above.

Pick the cube that looks best to *you*. Typically this will be *just above where gapping in the center starts to disappear*, but not so high that you start to see ridges. 

**If you can't decide, pick the higher one.**\
*Additionally, this is an aesthetics-first approach. If it looks good to you, it's good enough.* 

In this example, I chose the second cube, as this particular filament started to look nice and shiny with no gapping. Your particular filament may not shine like this (most don't.)

![](/images/EMPrints-Fine.png) 

### Too Low

Holding it up with the infill lines pointing towards a light source can help. This cube's EM is too low - you can see between the lines.

![](/images/em-light.png) 
### Slightly Too Low

These cubes need a little more EM - you can see slight gapping / valleys / shadows between the lines. 

A bit too high is better than a bit too low.

![](/images/EMPrints-SlightlyLow.png)

## Tips
**When I am looking for EM, I am *always* looking at the widest areas in a given print.** 

It's *totally normaly* for [:page_facing_up:smaller infill areas to look a bit overextruded](/articles/troubleshooting/small_infill_areas_overextruded.md). You want to tune for the areas where your extrusion system has had a chance to equalize pressure and coast at a constant flow rate.

In this example, I would primarily be looking at the circled area. 

While some of this print looks overextruded, I think the overall EM is actually pretty good.
- ![](/images/em-wheretolook.png) 
## Actual Prints with Tuned EM:

(standard ABS)
- ![](/images/EMPrint-Example.jpg) 
- ![](/images/EMPrint-Example4.png) 

(eSun ABS+ - more matte)
- ![](/images/EMPrint-Example2.jpg) 
- ![](/images/EMPrint-Example3.jpg) 