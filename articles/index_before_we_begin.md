---
layout: default
title: Before We Begin
nav_order: 2
has_children: true
---

# Before We Begin
## :warning: Important Checks
Before you follow *any* tuning methods in this guide, ensure that:
- Voron V2: I highly recommend following my [:page_facing_up: Voron V2 gantry squaring instructions ](./voron_v2_gantry_squaring.html) first.
- **:warning: Everything is tight (seriously, check again)**
    - Go back again and re-tighten *every single screw* you can possibly find, *especially* grub screws, linear rails, and everything in the toolhead. 
    - I do this once every once in a while, and I often find something that has shaken loose and is causing me issues that are *extremely* difficult to troubleshoot.
- **:warning: Your nozzle is not partially clogged.**
    - If your nozzle is partially clogged, you may not even notice. You may be able to print, but you will have an **extremely difficult time trying to tune**.
        - Ensure that you can easily extrude by hand with the filament latch open.
        - Ensure that the material falls straight down out of the nozzle when extruding midair. It should not shoot out to the side.
    - Hit it with a nozzle cleaning needle just in case.

- Your thermistors are the correct types in your config. Please double check them.
    - **:warning: If you use any NTC 100K B3950 thermistors**, update Klipper to the most recent version and change all instances of `sensor_type: NTC 100K beta 3950` to `sensor_type: Generic 3950` in your config. There was a [:page_facing_up: bug](https://github.com/Klipper3d/klipper/issues/4054) causing these thermistors to be inaccurate, which was fixed with a [:page_facing_up: recent deprecation.](https://github.com/Klipper3d/klipper/pull/4859)

        - Please note that some other features have been deprecated recently too. If you have not updated Klipper in a while, please see [:page_facing_up: here](https://gist.github.com/FHeilmann/a8097b3e908e85de7255bbe6246ddfd5) for instructions on how to fix up your config for the new Klipper version. 

            - You may also need to recompile/reflash your MCUs if you get a "command format mismatch" error after updating.
- Your motion components are clean, particularly between gear/pulley/idler teeth.
- Your nozzle is clean.
- Your nozzle has been tightened **while hot** (unless it's a Revo), and is not leaking material through the threads around the nozzle or heatbreak.