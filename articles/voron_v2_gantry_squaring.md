[:arrow_left: Back to Table of Contents](/README.md)
# Voron V2 Gantry Squaring

## Why?

Poor gantry squaring can cause a number of problems.\
Notice that the idlers get "pinched" when moving the X extrusion back/forth (this is shown with loose Z joints).

https://user-images.githubusercontent.com/34943186/154356504-b3870f34-32a3-4c2a-a424-7d48def0f834.mp4

This can potentially cause:
- First Layer issues
- Z belts rubbing against the gantry's printed parts

"Bonus" steps 14-16 can also help with first layer *and* with gantry stability.
## Method

**1)** Modify the `timeout` setting your `[idle_timeout]` config section. Set it to an arbitrarily high value (in seconds) and `reload`.
- This just gives us time to work. We need the Z motors to be energized and holding for the whole process.

**2)** `G28`, then `QUAD_GANTRY_LEVEL`. 

**3)** Jog your gantry to the center of the build volume using the LCD or web interface.
- This will give you space to work. You need easy access to both the bottom and top of your gantry.

**4)** Turn off ONLY your A/B motors using these g-codes:
- `SET_STEPPER_ENABLE STEPPER=stepper_x ENABLE=0`
- `SET_STEPPER_ENABLE STEPPER=stepper_y ENABLE=0`

**5)** Loosen your A/B belt tension fully.
- This prevents the A/B belt tension from pulling the gantry out of alignment while you work on it.
- Your belts should be fully disengaged. If there is still remaining tension with the idlers fully backed off, you may need to release the belt ends from the X carriage.

- ![](/images/Gantry-ABTension.png) 

**6)** Take off your left/right side panels.

**7)** Unscrew and drop your lower Z joints. 
- Your gantry will now be floating on just the belts.
    - Make sure your printer is on a fairly level surface, otherwise your gantry could swing too much to one side. (it doesn't have to be perfect, just don't do it on a hill),

- ![](/images/ZJoint-Lowered.png) 

- ![](/images/ZJoints-Lowered.png)

**8)** **PARTIALLY** loosen all connections to the extrusions.  
- You need all of these bolts to be loose enough to freely adjust against the printed part on the extrusions. 
- :warning::warning: Where there are Z belt clamps, **ensure that you do not loosen the bolts so much that the Z belts release**. Only loosen enough to allow for adjustments. :warning::warning: 

- X/Y joints (repeat for both sides). 
    - Top:
        - ![](/images/XYLoosen-Top.png) 

    - Bottom:
        - ![](/images/XYLoosen-Bottom.png) 

- A/B joints (repeat for both sides):
    - Top:
        - *Don't overdo the belt clamps!*
        - ![](/images/ABLoosen-Top.png) 

    - Bottom:
        - *Don't overdo the belt clamps!*
        - ![](/images/ABLoosen-Bottom.png) 

- Front idlers (repeat for both sides):
    - Top:
        - *Don't overdo it!*
        - ![](/images/IdlersLoosen-Top.png) 
    - Bottom:
        - *Don't overdo it!*
        - ![](/images/IdlersLoosen-Bottom.png) 

**9)** And now - what we have been prepping for! **Adjust your gantry so that it sits perfectly on top of the lower Z joints.**
- This involves moving gantry components further apart or closer together along the extrusions:
    - ![](/images/XAdjust.png) 

    - ![](/images/YAdjust.png)

- Your gantry should align so that:
    - The Z joints feel perfectly flush along the side, and
    - When raising and lowering your lower Z joint by hand, the bolt should slide in perfectly without hitting the sides.

    - ![](/images/Alignment-Side.png) ![](/images/Alignment-Hole.png) 

- Ensure that you do not inadvertently rotate your A/B joints during this process.
    - ![](/images/Alignment-AB-Good.png) 
    - (Exaggerated)\
    ![](/images/Alignment-AB-Bad.png) 

**10)** Tighten every extrusion bolt again, *except* those in the X/Y joints. (you will tighten those during step 12)
- Ensure that your Z joints still align properly. Sometimes tightening can move things around.

**11)** Re-install your lower Z joints and *lightly* tighten the M5 bolts.
- Do NOT hulk them down yet, or even make them tight. The "ball joint" should still be able to articulate completely freely.

**12)** Follow [:page_facing_up:Nero's de-racking video.](https://www.youtube.com/watch?v=cOn6u9kXvy0) 
- Make sure to come back here afterwards! The following steps are still important.

**13)** [:page_facing_up:Re-tension your A/B belts](https://docs.vorondesign.com/tuning/secondary_printer_tuning.html#belt-tension) (to 110hz **over a 15cm span**).
- Don't miss the video link in that post. It's easy to overlook.
- I prefer the Gates Carbon Drive app. Select the "motorcycle" option.

**14)** Reinstall your panels and fully heatsoak your printer for **1½ - 2 hours minimum.**

**15)** `QUAD_GANTRY_LEVEL` 3-5 times to "settle in" the gantry (and level it for the next step).
- If you are having new Z accuracy issues, you may have left your Z joints a bit *too* loose.

**16)** Open the front door and **fully hulk-tighten the M5 bolts in your Z joints*** while it's still hot.

\* *Unless your parts are printed in eSun ABS+. It's more brittle than regular ABS. Just tighten them "pretty tight".*
- This does two things:
    - Somewhat "locks in" your QGL at its state in full thermal expansion.
        - This has helped a number of people with their first layer issues.
    - **Stabilizes your gantry**. 
        - If you had it "tight but not too tight, so the Z joints can still articulate" (as is often recommended), you will notice that your gantry displaces back/forth while printing.
        - This can help with ringing and layer consistency.

**17)** Restore your `[idle_timeout]` settings (changed in step 1).
