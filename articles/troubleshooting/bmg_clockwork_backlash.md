[:arrow_left: Back to Table of Contents](/README.md)
# BMG Clockwork Backlash Issues (Repeating Patterns / "Wood Grain")

**Ensure that you have some [:page_facing_up:backlash](https://gfycat.com/mealycautiouscoqui) between the motor gear and the plastic gear.**
- Gauge this with filament loaded and the spring tensioned (the backlash will reduce a bit once it is loaded).
- You want a little backlash, but not *too* much.

This is adjusted by moving the motor itself up and down.\
The motor plate has 3 slotted screw holes to allow for adjustment:

![](/images/troubleshooting/Backlash-Adjust.png)

- The top two screws are easily reachable.
- The bottom left screw can be reached by opening the filament latch fully and using a ball-end hex driver.
## Too Little Backlash:
- [:pushpin:Repeating patterns](/articles/troubleshooting/bmg_clockwork_backlash.md#repeating-patterns) in extrusion

- Accelerated wear and damage of the plastic gear, further contributing to repeating patterns in extrusion.
    - This can cause permanent extrusion consistency issues until replacement. Check the spaces between the gear teeth. This gear is damaged:

    - ![](/images/troubleshooting/bmg-tooth-damage.png)


## Too Much Backlash:
- [:pushpin:Repeating patterns](/articles/troubleshooting/bmg_clockwork_backlash.md#repeating-patterns) in extrusion

- Clacking noises during retraction and pressure advance moves

## Repeating Patterns
- Adjusting backlash can help considerably with these issues, but is not always guaranteed to fix it.
- These issues can also be caused by poor quality BMG parts. Genuine Bondtech or Trianglelab BMG parts are best.
- Galileo/Orbiter seem to be less likely to have these extrusion patterns in my experience. Bowden systems are also less prone.
- Test prints: :page_facing_up:https://mihaidesigns.com/pages/inconsistent-extrusion-test
- **Examples:**
    - See [:page_facing_up:"Setting Expectations"](/articles/before_we_begin.md#setting-expectations)   
    - The left cube shows an "innie-outie" pattern across each extrusion line.\
    The right cube is with properly adjusted backlash, and the pattern is lessened.
        - ![](/images/troubleshooting/Backlash-Comparison.png)
    - "Wood Grain":
        - ![](/images/troubleshooting/Backlash-WoodGrain.png)
    - Diagonal patterns:\
    *Note: this kind of pattern can also be caused by mechanical issues with printer axes.*
        - ![](/images/troubleshooting/Backlash-Pattern.png)

## Mini Afterburner

I don't have a Mini Afterburner so I can't give an exact process for tweaking it. I believe it also has some slotted screw holes to allow for adjustment.

I have heard that loosening and threadlocking these screws may also help with its extrusion consistency:
- ![](/images/troubleshooting/Backlash-MiniAB-Screws)
