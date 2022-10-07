# Introduction

Much of this guide is specific to printers running **Klipper**. 

This guide was originally written for the Voron community, however all of the tuning sections should work on **any Klipper printer**. Some notes and hardware troubleshooting tips are still Voron specific, however.
## Notes

- My SuperSlicer profiles are located [:page_facing_up:here](https://github.com/AndrewEllis93/Ellis-PIF-Profile).
- If you have issues, comments, or suggestions about the guide, please let me know on GitHub issues or via Discord: [:page_facing_up:Ellis#4980](https://discordapp.com/users/207622442842062849)
    - For issues **not directly related to the guide content itself**, or for troubleshooting & print help, please use the public help channels in the [:page_facing_up:Voron Discord](https://discord.gg/voron) (or the appropriate community for your printer). 
- You can find the bed models and textures I am using [:page_facing_up:here](https://github.com/VoronDesign/Voron-Extras/tree/main/Bed_Models). The bed texture I am using in some of the older screenshots is from [:page_facing_up:VoronUsers.](https://github.com/VoronDesign/VoronUsers/tree/master/slicer_configurations/PrusaSlicer/hartk1213/V0/Bed_Shape) 
- Thank you to **bythorsthunder** for help with testing these methods and providing some of the photos.
- Support my drinking habits:
[![](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/paypalme/AndrewEllis93)

## Icons
- :warning: = **:exclamation:Please pay extra attention to items marked with this.:exclamation:**
- :page_facing_up: = Link to another page.
- :pushpin: = Jump to section (on same page).

# Table of Contents

## **Before We Begin**
- [Before We Begin](/articles/before_we_begin.md)
    - **:warning: Important Checks**
- [A Note About Line Width](/articles/a_note_about_line_width.md)
- [Setting Expectations](/articles/setting_expectations.md)

## **Print Tuning** 
*Essentials. Read/follow these in order shown.*
- [Build Surface Adhesion](/articles/build_surface_adhesion.md)
- [First Layer Squish](/articles/first_layer_squish.md)
- [Pressure Advance](/articles/pressure_advance.md)
    - Why PA is Needed
    - What PA Does
    - Lines Method
    - Fine-Tuning and What to Look For
    - [Tower Method](/articles/pressure_advance_tower_method.md) 
- [Extrusion Multiplier](/articles/extrusion_multiplier.md)
    - Background 
    - Method
    - Rationale & Dimensional Accuracy
- [PA / EM Oddities](/articles/pa_em_oddities.md)
    - Slight Perimeter Gapping
    - Slight Corner Gapping
- [Cooling and Layer Times](/articles/cooling_and_layer_times.md)
    - Signs of Overheating
    - How to Fix It
- [Retraction](/articles/retraction.md)
    - If You Are Having Persistent Issues
        - With PETG
- [Infill/Perimeter Overlap](/articles/infill_perimeter_overlap.md)

## **Printer Tuning**
*Mostly optional. For pushing limits, or for troubleshooting.\
"Voron V2 Gantry Squaring" is the only essential.*
- [Determining Maximum Volumetric Flow Rate](/articles/determining_max_volumetric_flow_rate.md)
    - Why?
    - Approximate Values
    - How Volumetric Flow Rate Relates to Print Speed
    - Formulas
    - Method
    - Flow Dropoff
- [Determining Motor Currents](/articles/determining_motor_currents.md)
    - Determining Initial `run_current`
    - Determining Maximum `run_current`
    - Determining `hold_current`
- [Determining Maximum Speeds and Accelerations](/articles/determining_max_speeds_accels.md)
    - Method
    - Usage of the `TEST_SPEED` Macro
- [Voron V2 Gantry Squaring](/articles/voron_v2_gantry_squaring.md)

## **Miscellaneous**
- [Stepover](/articles/stepover.md) (The black magic secret for better overhangs)
- [Useful Macros](/articles/useful_macros.md)
    - Conditional Homing
    - Conditional QGL
    - Beeper
    - LCD RGB
    - My Pause/Resume Macros (For Runouts, Filament Swaps, and Manual Pauses)
        - M600 (Filament Change) Alias
        - Example Filament Sensor Config
            - Basic Filament Switch Sensor
            - Smart Filament Sensor
        - Pause
        - Resume
        - Cancel
        - Octoprint Configuration 
    - Filament Sensor Management
    - Parking
    - Off
    - Shut Down Pi
        - As option in LCD menu
    - Dump Variables
    - Get Variable
    - Replace `M109`/`M190` With `TEMPERATURE_WAIT`
- [Passing Slicer Variables to PRINT_START](/articles/passing_slicer_variables.md)
    - Passing Temperatures
        - SuperSlicer
        - Prusa Slicer
        - Cura
- [Controlling Slicer Temperature G-Code Order (Simple Method)](/articles/controlling_slicer_g-code_order.md)
- [My Setup](/articles/my_setup.md) (since people ask a lot)

## **Troubleshooting**
*Even without issues, you should look through these to fmiliarize yourself with things to look out for. **Especially** thermal drift under "First Layer / Squish Consistency Issues"*
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
    - Mechanical
    - Speeds and Accelerations
    - Electrical
- [PLA is Overheating](/articles/troubleshooting/pla_overheating.md)
- [Pockmarks](/articles/troubleshooting/pockmarks.md)
- [VFAs (Vertical Fine Artifacts)](/articles/troubleshooting/vfas.md)
    - Repeating VFAs With ~2mm Spacing
    - Repeating VFAs With Non-2mm Spacing
- [Slicer is Putting Heating G-codes in the Wrong Place/Order](/articles/troubleshooting/slicer_putting_heating_g-codes_wrong_order.md)
- [Small Infill Areas Look Overextruded](/articles/troubleshooting/small_infill_areas_overextruded.md)