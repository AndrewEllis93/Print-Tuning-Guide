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

## The Magic Bullet (But With Downsides)
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

### Making it Faster (Still With Downsides)
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

---
## When assessing extrusion multiplier, *always* look at the widest areas in a given print.
(Excerpt from the [:page_facing_up:Extrusion Multiplier](/articles/extrusion_multiplier.md) article)
- You want to tune your extrusion multiplier for the areas where your extrusion system has had a chance to equalize pressure and coast at a constant flow rate.
- In this example, I would primarily be looking at the circled area. 
- While some of this print looks overextruded, I think the overall EM is actually pretty good.
    - ![](/images/em-wheretolook.png) 

---

[:arrow_left: Back to Table of Contents](/README.md)