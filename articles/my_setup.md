---
layout: default
title: My Setup
nav_order: 11
---
{% comment %} 
# This page has moved! Please visit [the new location](https://ellis3dp.com/Print-Tuning-Guide/articles/my_setup.html).
{% endcomment %}
# My Setup

Voron V2.4 350mm (with some V2.2 parts still on it)
- **Toolhead**
    - [:page_facing_up: Stealthburner toolhead](https://github.com/VoronDesign/Voron-Stealthburner)
    - [:page_facing_up: Orbiter 1.5 extruder](https://www.aliexpress.com/item/3256803143364574.html) (LDO motor version) - mounted with [:page_facing_up: this mod](https://www.teamfdm.com/files/file/502-orbiter-15-for-stealthburner/)
    - Rapido UHF with Bondtech CHT Volcano 0.4mm nozzle
- **Hardware Upgrades**
    - [:page_facing_up: Fabreeko HoneyBadger textured PEI](https://www.fabreeko.com/products/honeybadger-v2-4-single-sided-black-pei-textured?variant=42614568452351)
    - LDO-42STH40-2004MAH(VRN) A/B motors
        - Honestly I'd stick with the OMC motors from the sourcing guide. Didn't get much quality increase out of the upgrade to 0.9° motors, just lower speeds :clown_face:
    - Single Hiwin MGN9 rail on X
    - [:page_facing_up: Genuine Gates brand pulleys/idlers](https://www.filastruder.com/search?type=product&q=gates) in gantry
    - [:page_facing_up: BTT Smart Filament Sensor](https://www.aliexpress.us/item/2255800154703522.html)
- **Mods**
    - [:page_facing_up: Euclid](https://euclidprobe.github.io) (using Klicky macros) w/ [:page_facing_up: auto z calibration](https://github.com/protoloft/klipper_z_calibration)
    - Chamber thermistor
    - [:page_facing_up: Bed fans](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/Ellis/Bed_Fans)
    - Umbilical 
        - i.e. "flappy cable". No X/Y cable chains. 
        - This saves a fair bit of weight on the X axis, and I have not had a single wire break since (I had a lot of wire breaks with cable chains and got sick of them.) It's also WAY easier to service. You do lose a bit of Z height, though.
        - I just did this the janky way - I just wrapped the wires up and zip tied the far end to the Z chain, and the toolhead side to the reverse bowden tube. There are prettier mods out there for it.
    - Toolhead X endstop & [:page_facing_up: relocated Y endstop](https://github.com/hartk1213/MISC/tree/main/Voron%20Mods/Voron%202/2.4/Voron2.4_Y_Endstop_Relocation)
        - Allows for umbilical.
        - The Y endstop relocation is also available as part of the pin mod below.
        - The toolhead X endstop is my own mod, and is outdated now. Not sure what other options are currently available, haven't looked into it.
    - [:page_facing_up: Pin mod](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/hartk1213/Voron2.4_Trident_Pins_Mod)
    - [:page_facing_up: GE5C mod](https://github.com/hartk1213/MISC/tree/main/Voron%20Mods/Voron%202/2.4/Voron2.4_GE5C)
    - Gantry backers
        - [:page_facing_up: MGN9 Y backers](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/bythorsthunder/MGN9_Backers)
        - [:page_facing_up: Titanium X backer](https://www.fabreeko.com/products/v2-4-trident-titanium-extrusion-backers?variant=40722088034502) 
        - These prevent the gantry from [:page_facing_up: warping with heat.](https://github.com/tanaes/whopping_Voron_mods/tree/main/extrusion_backers)
    - Frame thermistor
        - Used for sofware frame thermal expansion compensation (to combat thermal drift. Allows me to print from cold, without heat soaking. Though I do still wait for a minimum chamber temp to be reached.)
            - There are some more links about this in [:page_facing_up: Thermal Drift](./troubleshooting/first_layer_squish_consistency_issues/thermal_drift.md).
    - [:page_facing_up: Decontaminator nozzle brush](https://github.com/VoronDesign/VoronUsers/tree/master/orphaned_mods/printer_mods/edwardyeeks/Decontaminator_Purge_Bucket_%26_Nozzle_Scrubber)
    - Voron V2.2 handles & single panel front door
    - PiCam with some random Thingiverse mount
    - [:page_facing_up: Annex Engineering twist-lock panel clips](https://github.com/Annex-Engineering/Other_Printer_Mods/tree/master/All_Printers/Annex_Panel_2020_Clips_and_Hinges)