---
layout: default
title: Misconceptions & Bad Advice
nav_order: 9
---

# Misconceptions & Bad Advice
{: .no_toc }

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

This is just a list of things that I often see floating around that are, in my opinion, misconceptions or bad advice.

## Two 0.4mm Perimeters = 0.8mm

The title is just an example, this applies to any line width or perimeter count.

- I'm using 0.4mm for simplicity, even though I generally recommend printing line widths larger than nozzle diameter.


Two 0.4mm perimeters **does not equal 0.8mm.**

The "spacing" (center-to-center distance - 0.357 in the below example) is not equal to the line width. It's determined using this formula:
- spacing = extrusion_width - layer_height * (1 - PI/4)\
<sup>[Source](https://manual.slic3r.org/advanced/flow-math)</sup>

At 0.2mm layer height, two perimeters actually equals **0.757mm!**
- ![](./images/misconceptions/spacing.png)

    - And then three perimeters would equal **1.114mm!**

        - ![](./images/misconceptions/spacing_3x.png)


### If You Want Clean Multiples (SuperSlicer Only)
If you want two walls to equal a clean multiple like you may expect, SuperSlicer allows you to specify **spacings** rather than line widths.

You would put a **spacing** *(or "width & spacing combo" for external perimeters)* of 0.4mm / 100% rather than a **line width** of 0.4mm / 100%:
- ![](./images/misconceptions/ss_spacing.png)

- Then two lines would equal 0.8mm, three lines would equal 1.2mm, and so on.


## Tuning Extrusion Multiplier By Measuring 1-2 Cube Walls

When measuring two walls, you run into the [:pushpin: issue described above](#two-04mm-perimeters--08mm). Two walls does **NOT equal line width * 2**!

In both cases, you are also measuring **layer wobble and inconsistent extrusion**, which all printers and filaments have in some degree. You will always be measuring the bit that sticks out most.

{% comment %} 

Please excuse the upcoming vomit I used to bodge this table's widths/spacing

{% endcomment %} 


| <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Layer Wobble** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br> | <br>**Inconsistent Extrusion /**<br>&nbsp;&nbsp;&nbsp;&nbsp;**Filament Diameter Fluctuations**&nbsp;&nbsp;&nbsp;&nbsp;<br><br> |
| :-----------: | :-----------: |
| <br>![](./images/misconceptions/layer_wobble_marked.png)<br><br> | ![](./images/misconceptions/extrusion_inconsistency_marked.png) |

- Your measurement will basically **always** be a bit too large because of this!

- Additionally, when making small measurements like this, **small errors become big errors**:

    - For example, the difference between 0.42mm and 0.4mm, an only 0.**0**2mm difference, is about **5%**.

        - **That's a huge adjustment!** It's very easy to measure 0.02mm off - due to consumer-grade calipers, where you measure, how much layer wobble you have, how much pressure you use, the diameter fluctuations of your filament, what you ate for breakfast, etc...

            - You should always make dimensional adjustments based on **larger objects**, where minor errors are proportionally much smaller.*

            \* *I actually don't like adjusting extrusion multiplier based on measurements at all. But that's more debatable.\
        In my opinion, it's best to print an object with 100% solid infill and tune extrusion multiplier until it fills perfectly without going over. See [:page_facing_up: here](./extrusion_multiplier.md) for specific instructions. Then adjust things like shrinkage compensation in the slicer.\
        I don't think it makes sense to have a gappy or rough print just to compensate for dimensions.*

**This method is, much to my chagrin, extremely prevalent:**
- [https://teachingtechyt.github.io/calibration.html#flow](https://teachingtechyt.github.io/calibration.html#flow)\
You may notice this guide popping up a lot on this page, as I add more sections....
- [https://help.prusa3d.com/article/extrusion-multiplier-calibration_2257](https://help.prusa3d.com/article/extrusion-multiplier-calibration_2257)\
Even Prusa recommends it!
- [https://3dprintbeginner.com/flow-rate-calibration/](https://3dprintbeginner.com/flow-rate-calibration/)

<sup>Send help. I'm going insane.</sup>


## "You Shouldn't Tune Extrusion Multiplier"

The gap between theory and reality is often larger in reality than it is in theory.

More info to come...

## Calibrating Belted Axis Steps

Don't mess with your axes!

More info to come...

## Using Paper to Set Z Offset

More info to come...


{% comment %} 

## "You Should use 100% Extrusion Multiplier"

- https://youtu.be/YPAXeBuq9qU?t=869

## Calibrating Belted Axis Steps

- https://youtu.be/YPAXeBuq9qU?t=166 *(you might notice that this is the third time this video has appeared on this list...)*
- https://teachingtechyt.github.io/calibration.html#xyzsteps
- https://all3dp.com/2/how-to-calibrate-a-3d-printer-simply-explained/
- https://www.3dbeginners.com/how-to-calibrate-a-3d-printer/

<sup>SEND HELP. I'M GOING INSANE.</sup>




{% endcomment %} 