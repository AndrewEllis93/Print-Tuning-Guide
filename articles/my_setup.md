# My Setup

Voron V2.4 350mm
- **Toolhead**
    - [AB-BN-30](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/Badnoob/AB-BN)
        - Stealthburner will replace this.
    - Trianglelab Dragon High Flow
        - If I were buying today, I'd get a Rapido.
    - Orbiter 1.5
- **Hardware Upgrades**
    - LDO-42STH40-2004MAH(VRN) A/B motors
    - Single Hiwin MGN9 rail on X
    - Genuine gates pulleys/idlers in gantry
    - [BTT Smart Filament Sensor](https://www.amazon.com/BIGTREETECH-Filament-Sensor-Detection-Printer/dp/B07Z7Y5VY9)
- **Mods**
    - [Klicky](https://github.com/jlas1/Klicky-Probe) w/ [auto z calibration](https://github.com/protoloft/klipper_z_calibration)
    - Chamber thermistor
    - [Bed fans](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/Ellis/Bed_Fans)
    - Umbilical 
        - i.e. "flappy cable". No X/Y cable chains. 
        - This saves a fair bit of weight on the X axis, and I have not had a single wire break since (I had a lot of wire breaks with cable chains and got sick of them.) It's also WAY easier to service. You do lose a bit of Z height, though.
        - I just did this the janky way - I just wrapped the wires up and zip tied the far end to the Z chain, and the toolhead side to the reverse bowden tube. There are prettier mods out there for it.
    - Toolhead X endstop & A drive Y endstop 
        - Allows for umbilical.
        - A drive Y endstop is part of the pin mod below.
        - The toolhead X endstop is my own mod, and is outdated now. Not sure what other options are currently available, haven't looked into it.
    - [Pin mod]()
    - [GE5C mod](https://github.com/hartk1213/MISC/tree/main/Voron%20Mods/Voron%202/2.4/Voron2.4_GE5C)
    - Gantry backers
        - [MGN9 Y backers](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/bythorsthunder/MGN9_Backers)
        - Titanium X backer
        - These prevent the gantry from [warping with heat.](https://github.com/tanaes/whopping_Voron_mods/tree/main/extrusion_backers)
    - Frame thermistor
        - Used for sofware frame thermal expansion compensation (to combat thermal drift. Allows me to print from cold, without heat soaking. Though I do still wait for a minimum chamber temp to be reached.)
            - This is a giant rabbit hole, be warned. Please don't ask me for help with this (sorry)
    - [Decontaminator nozzle brush](https://github.com/VoronDesign/VoronUsers/tree/master/abandoned_mods/printer_mods/edwardyeeks/Decontaminator_Purge_Bucket_%26_Nozzle_Scrubber)
    - [Annex Engineering twist-lock panel clips](https://github.com/Annex-Engineering/Other_Printer_Mods/tree/master/All_Printers/Annex_Panel_2020_Clips_and_Hinges)


Excuse the hazy panels. Fact of life with ABS.

![](/images/my_setup.jpg)