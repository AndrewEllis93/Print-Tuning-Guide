[:arrow_left: Back to Table of Contents](/README.md)

---
# Small Infill Areas Look Overextruded

![](/images/troubleshooting/SmallAreas.png) 

**Some amount of this is unavoidable and is totally normal.**\
But, there are some things that *may* help a bit:
- Use single top perimeters (SuperSlicer). This simply makes these infill areas a bit larger.
- Try reducing your pressure advance smooth time (I use 0.02).
    - Direct drive can handle lower smooth times than bowden. Going too low will cause extruder skipping during PA movements.
        - Run the PA pattern test afterwards to make sure you haven't introduced any skipping.
    - **There seem to be diminishing returns here**, at least in my testing. There's no need to tune this down as low as physically possible.
- Try reducing top infill speeds and accelerations.
    - Again, there are diminishing returns here. On my printer, I stop seeing noticeable improvements below around 2k acceleration. Your mileage may vary.
- In SuperSlicer: Try setting top infill to "not connected" (`infill_connection_top`).
    - "Not connected" needs lower infill/perimeter enchroachment (`infill_overlap`)* than "connected" does. You may need to lower this. Reset it to default (to start).
        - *Unfortunately it overshoots the perimeters a little bit in my opinion. Setting your `infill_overlap` too low to compensate will also affect sparse infill (and therefore strength), so don't go too low.
    - This is the default behavior in Cura, and is not possible in Prusa Slicer. 
- Ensure that your extruder gears don't have too much [:page_facing_up:backlash](https://gfycat.com/mealycautiouscoqui). 
    - You **want** a tiny amount of backlash (but as little as possible - this is just to make sure that you haven't over tensioned the gears. Too much tension can cause [:page_facing_up:extrusion patterns](/articles/troubleshooting/extrusion_patterns.md) and accelerated wear.) 
    - Too much backlash can cause issues with pressure advance and retractions.
    - You may need to re-tune PA (and sometimes esteps) after adjusting this.
    - This is not adjustable on some extruders like the Orbiter (doesn't have the same backlash issues anyway in my experience!)
- Sometimes you can change your infill angle to improve things for a particular piece, but this is highly geometry dependent.
    - Concentric top infill patterns can help with some STLs, but again, it's highly geometry dependent (and the aesthetics are a bit divisive).

---

### **When assessing extrusion multiplier, *always* look at the widest areas in a given print.** 

You want to tune your extrusion multiplier for the areas where your extrusion system has had a chance to equalize pressure and coast at a constant flow rate.

In this example, I would primarily be looking at the circled area. 

While some of this print looks overextruded, I think the overall EM is actually pretty good.

- ![](/images/em-wheretolook.png) 

---
:bulb: I'm still testing different ideas, let me know if you have any, or are able to reliably reproduce improvements in [:page_facing_up:this](https://github.com/VoronDesign/Voron-2/blob/Voron2.4/STLs/Test_Prints/Heatset_Practice.stl) test piece.

Here are some ideas I have yet to thoroughly test. Let me know if you try them.
- What is the affect of different temperatures? Maybe viscosity has an effect?
- Is the issue worse with higher flow hotends?
- Does "Enforce 100% fill volume" in SuperSlicer do anything? I can't see any changes, but some people say it helped (I'm suspecting placebo).
- Does square_corner_velocity have an effect?
---

[:arrow_left: Back to Table of Contents](/README.md)