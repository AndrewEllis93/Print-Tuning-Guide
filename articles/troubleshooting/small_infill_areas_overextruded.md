[:arrow_left: Back to Table of Contents](/README.md)
# Small Infill Areas Look Overextruded

![](/images/troubleshooting/SmallAreas.png) 

Some amount of this is unavoidable, but there are some things that *may* help:
- Use single top perimeters (SuperSlicer). This simply makes these infill areas a bit larger.
- Try reducing your pressure advance smooth time (I use 0.02)
    - Direct drive can handle lower smooth times than bowden. Going too low will cause extruder skipping during PA movements.
- Try reducing top infill speeds and accelerations.
- UNTESTED: Some people have told me that disabling "Enforce 100% fill volume" in SuperSlicer can help. I have not yet had time to verify this.


**When I am looking for EM, I am *always* looking at the widest areas in a given print.** 

You want to tune your extrusion multiplier for the areas where your extrusion system has had a chance to equalize pressure and coast at a constant flow rate.

In this example, I would primarily be looking at the circled area. 

While some of this print looks overextruded, I think the overall EM is actually pretty good.

- ![](/images/em-wheretolook.png) 