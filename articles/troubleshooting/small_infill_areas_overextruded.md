[:arrow_left: Back to Table of Contents](/README.md)

---
# Small Infill Areas Look Overextruded

![](/images/troubleshooting/small_infill_overextruded/example1.png) 

**Some amount of this is unavoidable and is totally normal.**\
But, there are some things that *may* help a bit:
- Use single top perimeters (SuperSlicer). This simply makes these infill areas a bit larger.
- Try reducing your pressure advance smooth time (I use 0.02).
    - Direct drive can handle lower smooth times than bowden. Going too low will cause extruder skipping during PA movements.
        - Run the PA pattern test afterwards to make sure you haven't introduced any skipping.
    - **There seem to be diminishing returns here**, at least in my testing. There's no need to tune this down as low as physically possible.
- Try reducing top infill speeds and accelerations.
    - Again, there are diminishing returns here. On my printer, I stop seeing noticeable improvements below around 2k acceleration. Your mileage may vary.
- Ensure that your extruder gears don't have too much [:page_facing_up:backlash](https://gfycat.com/mealycautiouscoqui). 
    - You **want** a tiny amount of backlash (but as little as possible - this is just to make sure that you haven't over tensioned the gears. Too much tension can cause [:page_facing_up:extrusion patterns](/articles/troubleshooting/extrusion_patterns.md) and accelerated wear.) 
    - Too much backlash can cause issues with pressure advance and retractions.
    - You may need to re-tune PA (and sometimes esteps) after adjusting this.
    - This is not adjustable on some extruders like the Orbiter (doesn't have the same backlash issues anyway in my experience!)
- Sometimes you can change your infill angle to avoid short infill lines, but this is highly geometry dependent.
    - Concentric top infill patterns can help with some STLs, but again, it's highly geometry dependent. (And the aesthetics are love-it-or-hate-it).

## "Not Connected" Top Infill (SuperSlicer)
I find that setting top infill to "not connected"  makes a noticeable improvement.\
This is default behavior in Cura, and is not available in Prusa Slicer.

- ![](/images/troubleshooting/small_infill_overextruded/not_connected_setting.png)
- :warning: This setting overshoots perimeters more than "connected" does. If you have raised your infill/perimeters encroachment (overlap), **consider setting it back to default** (for now. You can fine-tune later).
    - Overshoot
        - ![](/images/troubleshooting/small_infill_overextruded/overshoot.png)
    - Reset infill/perimeter encroachment
        - ![](/images/troubleshooting/small_infill_overextruded/encroachment_setting.png)
        - **:warning: Don't set it too low, however, as it also affects sparse infill**. A low value can cause sparse infill to become detached from the perimeters:
            - ![](/images/troubleshooting/small_infill_overextruded/infill_disconnect.png)
### What it Does

- ![](/images/troubleshooting/small_infill_overextruded/connected_not_connected_comparison.png)

## The Magic Bullet? (But With Downsides)
---

Disclaimer: I am **not** using this trick in my daily driver profiles due to the drawbacks.\
I am only using the "not connected" settings described above, with 25% overlap/enchroachment.

If you are having small infill issues, it may still be worth a try, however.

- I'm currently tinkering with the SuperSlicer source code to possibly add a "minimum travel after z-hop" setting, just like the "minimum travel after retraction" setting.
- :bulb:*If you're familiar with C++ and willing to help me out here, I would be grateful! I don't think it's a super difficult change, I'm just very much stumbling my way through this and currently failing.*

---

This setting has yielded the largest improvement of all for me. Your mileage may vary of course, but I'm curious to hear your experiences with it.

**In combination with** the "not connected" top infill setting described above, you can set "minimum travel after retraction" to 0.\
This will cause a retraction at every direction change. 

:warning: **This is very slow with Z hop, however**. These successive Z hops can also be **quite loud** on many printers.

<sup>*(See [:pushpin:next section](#making-it-faster-still-with-downsides) for a potential speed improvement)*</sup>
- Setting
    - ![](/images/troubleshooting/small_infill_overextruded/retract_setting.png)

- Each purple spot is a retraction.
    - ![](/images/troubleshooting/small_infill_overextruded/not_connected_retractions.png)

- Excessive Z hopping.
    - ![](/images/troubleshooting/small_infill_overextruded/retract_min_distance_example_hop_on.png)

### Making it Faster (Still With Some Downsides)
- You can turn Z hop off for *only* the top layer, like so:

    - ![](/images/troubleshooting/small_infill_overextruded/hop_setting.png)

    - Result
        - ![](/images/troubleshooting/small_infill_overextruded/retract_min_distance_example_hop_off.png)

- This is considerably faster and quieter, however it too carries some downsides:
- :warning: **Downsides**
    - It will still be slower than standard, but not nearly as much as with z-hop. The top layers are something like 30% slower, if I had to guess.
    - Disabling Z hop on the top layer carries some risk of:
        - Minor surface scarring during travels
        - Knocking over parts if you have excessive curling

### Solid Infill Considerations
- Further small improvements may be made by also setting solid infill to "not connected".
- However, :warning: make sure you also check "only retract when crossing perimeters".

- ![](/images/troubleshooting/small_infill_overextruded/not_connected_solid_setting.png)

- ![](/images/troubleshooting/small_infill_overextruded/only_retract_when_crossing_perimeters_setting.png)

- :warning: Otherwise, these additional retractions (and the slowdown!) will occur on **ALL solid layers, not just the top.**

    - ![](/images/troubleshooting/small_infill_overextruded/not_connected_retractions_solid.png)

### Demonstration

All samples with "not connected" are shown with [:pushpin:top retractions](#the-magic-bullet-but-with-downsides) **enabled**.

Lower overlaps show more small improvements, but also start to create pinholes.

In my case, I decided to stick with NC/NC/25%. Still a nice improvement.\
Anything lower would create [:page_facing_up:pinholes](/articles/infill_perimeter_overlap.md), and as mentioned in [:pushpin:this section](#the-magic-bullet-but-with-downsides), too low would start to disconnect the infill.

- ![](/images/troubleshooting/small_infill_overextruded/demonstration.png)

### My (Personal) Final Settings
- **Top:** "Not connected"
- **Solid:** "Not connected"
- **Overlap (encroachment):** 25%

I decided not to use the retraction trick in my daily driver for the time being, due to the top scarring concerns.

---
## When assessing extrusion multiplier, *always* look at the widest areas in a given print.
(Excerpt from the [:page_facing_up:Extrusion Multiplier](/articles/extrusion_multiplier.md) article)
- You want to tune your extrusion multiplier for the areas where your extrusion system has had a chance to equalize pressure and coast at a constant flow rate.
- In this example, I would primarily be looking at the circled area. 
- While some of this print looks overextruded, I think the overall EM is actually pretty good.
    - ![](/images/em-wheretolook.png) 

---

[:arrow_left: Back to Table of Contents](/README.md)