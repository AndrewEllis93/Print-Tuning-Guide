# Introduction

Much of this guide is specific to printers running **Klipper**. 

This guide was originally written for the Voron community, however all of the tuning sections should work on **any Klipper printer**. Some of the bullet points and hardware troubleshooting tips are still Voron specific, however.

**:warning: Please pay special attention to anything bolded and marked with ":warning:"**

My SuperSlicer profiles are located [:page_facing_up:here](https://github.com/AndrewEllis93/Ellis-PIF-Profile).

If you have issues, comments, or suggestions, please let me know on Discord: [:page_facing_up:Ellis#4980](https://discordapp.com/users/207622442842062849)

You can find bed the models and textures I am using in [:page_facing_up:Hartk's GitHub repo](https://github.com/hartk1213/MISC/tree/main/Voron%20Mods/SuperSlicer). The bed texture I am using is an older one from him in [:page_facing_up:VoronUsers.](https://github.com/VoronDesign/VoronUsers/tree/master/slicer_configurations/PrusaSlicer/hartk1213/V0/Bed_Shape) 

Thank you to **bythorsthunder** for help with testing these methods and providing some of the photos.

[![](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/paypalme/AndrewEllis93)

# Table of Contents
- Before We Begin
    - [Before We Begin](/articles/before_we_begin.md)
        - **:warning: Important Checks**
        - A Note About Line Width
        - Setting Expectations
- **Print Tuning** \
**(Follow these in order shown)**
    - [First Layer Squish](/articles/first_layer_squish.md)
        - Method
        - Print Examples
    - [Build Surface Adhesion](/articles/build_surface_adhesion.md)
    - [Pressure Advance](/articles/pressure_advance.md)
        - Lines Method
        - Tower Method
        - Fine-Tuning and What to Look For
    - [Extrusion Multiplier](/articles/extrusion_multiplier.md)
        - Background 
        - Methods I'm Not a Fan Of
        - Method
        - The Relationship Between Pressure Advance & EM
    - [Cooling and Layer Times](/articles/cooling_and_layer_times.md)
        - Signs of Overheating
        - How to Fix It
    - [Retraction](/articles/retraction.md)
    - [Infill/Perimeter Overlap](/articles/infill_perimeter_overlap.md)
- **Printer Tuning**
    - [Determining Maximum Volumetric Flow Rate](/articles/determining_max_volumetric_flow_rate.md)
        - Why?
        - Approximate Values
        - How Volumetric Flow Rate Relates to Print Speed
        - Method
    - [Determining Motor Currents](/articles/determining_motor_currents.md)
    - [Determining Maximum Speeds and Accelerations](/articles/determining_max_speeds_accels.md)
        - Method
        - Usage of the TEST_SPEED Macro
    - [Voron V2 Gantry Squaring](/articles/voron_v2_gantry_squaring.md)
- **Miscellaneous**
    - [Passing Slicer Variables to PRINT_START](/articles/passing_slicer_variables.md)
    - [Controlling Slicer G-code Order *Without* Passing Variables](/articles/controlling_slicer_g-code_order.md)
- **Troubleshooting**
    - [BMG Clockwork Backlash Issues (Repeating Patterns / "Wood Grain")](/articles/troubleshooting/bmg_clockwork_backlash.md)
    - [Bulging](/articles/troubleshooting/bulging.md)
        - Bulging Layers
        - Bulges at STL Vertices
        - Bulging Patterns on Overhangs (SS)
    - [Crimps](/articles/troubleshooting/crimps.md)
    - [Error: "Command Format Mismatch"](/articles/troubleshooting/command_format_mismatch.md)
    - [Extruder Skipping](/articles/troubleshooting/extruder_skipping.md)
    - [First Layer / Squish Consistency Issues](/articles/troubleshooting/first_layer_squish_consistency.md)
        - Thermal Drift
        - First Layer Conistency
        - Squish Consistency (Between Prints)
    - [Layer Shifting](/articles/troubleshooting/layer_shifting.md)
        - Electrical
        - Mechanical
        - Speeds and Accelerations
    - [PLA is Overheating](/articles/troubleshooting/pla_overheating.md)
    - [Pockmarks](/articles/troubleshooting/pockmarks.md)
    - [VFAs (Vertical Fine Artifacts)](/articles/troubleshooting/vfas.md)
        - Repeating VFAs With ~2mm Spacing
        - Repeating VFAs With Non-2mm Spacing
    - [Slicer is Putting Heating G-codes in the Wrong Place/Order](/articles/troubleshooting/slicer_putting_heating_g-codes_wrong_order.md)
    - [Small Infill Areas Look Overextruded](/articles/troubleshooting/small_infill_areas_overextruded.md)