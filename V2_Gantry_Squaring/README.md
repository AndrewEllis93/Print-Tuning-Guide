# Voron V2 Gantry Squaring

## Why?

Poor gantry squaring can cause a number of problems.
Notice that the idlers get "pinched" when moving the X extrusion back/forth (this is shown with loose Z joints).

https://user-images.githubusercontent.com/34943186/154356504-b3870f34-32a3-4c2a-a424-7d48def0f834.mp4

This can cause a number of problems, primarily:
- First Layer issues
- Z belts rubbing against the gantry's printed parts

## Method

**1)** Modify your `idle_timeout` in your config to an arbirarily high number, then `reload`. 
- This just gives us time to work. We need the motors to be energized and holding for the whole process.

**2)** `G28`, then `QUAD_GANTRY_LEVEL`. 

**3)** Jog your gantry to around the center of the build volume using the LCD or web interface.
- This will give you space to work. You need easy access to both the bottom and top of your gantry.

**4)** Loosen your A/B belt tension fully.
- This prevents the A/B belt tension from pulling the gantry out of alignment while you work on it.

- ![](Images/Gantry-ABTension.png) 

**5)** Take off your left/right side panels.

**6)** Unscrew and drop your lower Z joints. Your gantry will now be floating on just the belts.

- ![](Images/ZJoint-Lowered.png) 

- ![](Images/ZJoints-Lowered.png)

**7)** **PARTIALLY** loosen all connections to the extrusions.  
- You need all of these bolts to be loose enough to freely adjust against the printed part on the extrusions. 
- **(!!!!!!)** Where there are Z belt clamps, **ensure that you do not loosen the bolts so much that the Z belts release**. Only loosen enough to allow for adjustments.

- X/Y joints (repeat for both sides). 
    - Top:
        - ![](Images/XYLoosen-Top.png) 

    - Bottom:
        - ![](Images/XYLoosen-Bottom.png) 

- A/B joints (repeat for both sides):
    - Top:
        - *Don't overdo the belt clamps!*
        - ![](Images/ABLoosen-Top.png) 

    - Bottom:
        - *Don't overdo the belt clamps!*
        - ![](Images/ABLoosen-Bottom.png) 

- Front idlers (repeat for both sides):
    - Top:
        - *Don't overdo it!*
        - ![](Images/IdlersLoosen-Top.png) 
    - Bottom:
        - *Don't overdo it!*
        - ![](Images/IdlersLoosen-Bottom.png) 

**8)** And now - what we have been prepping for! **Adjust your gantry so that it sits perfectly on top of the lower Z joints.**
- This involves moving gantry components further apart or closer together along the extrusions:
    - ![](Images/XAdjust.png) 

    - ![](Images/YAdjust.png)

- Your gantry should align so that:
    - The Z joints feel perfectly flush along the side, and
    - When raising and lowering your lower Z joint by hand, the bolt should slide in perfectly without hitting the sides.

    - ![](Images/Alignment-Side.png) ![](Images/Alignment-Hole.png) 

- Ensure that you do not inadvertently rotate your A/B joints during this process.
    - ![](Images/Alignment-AB-Good.png) 
    - (Exaggerated)
    - ![](Images/Alignment-AB-Bad.png) 

**9)** Tighten every extrusion connection in the gantry again **except** for the X/Y joints.

**10)** Ensure that the lower Z joints still slide nicely into the upper Z joints after tightening.

**11)** Re-install your lower Z joints and *lightly* tighten the M5 bolts.
- Do NOT hulk them down yet. The "ball joint" should still be able to articulate completely freely.

**12)** Follow [Neros' de-racking video.](https://www.youtube.com/watch?v=cOn6u9kXvy0) 
- Make sure to come back here afterwards! The following steps are still important.

**13)** Reinstall your panels and fully heatsoak your printer for **1½ - 2 hours minimum.**

**14)** `QUAD_GANTRY_LEVEL` 3-5 times to "settle in" the gantry (and level it for the next step).

**15)** Open the front door and **fully hulk-tighten the M5 bolts in your Z joints.** Don't take too long.
- **This is extremely important.** 
    - This does two things:
        - Somewhat "locks in" your QGL at its state in full heatoak.
            - This has helped a number of people with their first layer issues.
        - **Stabilizes your gantry**. 
            - If you had it "tight but not too tight, so the Z joints can still articulate" (as is often recommended), you will notice that your gantry displaces back/forth while printing.
            - This can help with ringing and layer consistency.

**16)** Restore your `idle_timeout` settings (changed in step 1).
