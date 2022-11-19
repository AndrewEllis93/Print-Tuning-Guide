# Introduction

Some parts of this guide are tailored to printers running **Klipper**, but many pages work for other firmwares. See "Compatibility Icons" below.

This guide was originally written for the Voron community. Some notes and hardware troubleshooting tips are still Voron specific.
## Notes

- My SuperSlicer profiles are located [:page_facing_up:here](https://github.com/AndrewEllis93/Ellis-SuperSlicer-Profiles).
- If you have issues, comments, or suggestions about the guide, please let me know on GitHub issues or via Discord: [:page_facing_up:Ellis#4980](https://discordapp.com/users/207622442842062849)
    - For issues **not directly related to the guide content itself**, or for troubleshooting & print help, please use the public help channels in the [:page_facing_up:Voron Discord](https://discord.gg/voron) (or the appropriate community for your printer). 
- You can find the bed models and textures I am using [:page_facing_up:here](https://github.com/VoronDesign/Voron-Extras/tree/main/Bed_Models). The bed texture I am using in some of the older screenshots is from [:page_facing_up:VoronUsers.](https://github.com/VoronDesign/VoronUsers/tree/master/slicer_configurations/PrusaSlicer/hartk1213/V0/Bed_Shape) 
- Thank you to **bythorsthunder** for help with testing these methods and providing some of the photos.
- Support my drinking habits:
[![](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/paypalme/AndrewEllis93)
- Icons
    - :warning: = **:exclamation:Please pay extra attention to items marked with this.:exclamation:**
    - :page_facing_up: = Link to another page.
    - :pushpin: = Jump to section (on same page).


# Table of Contents
#### Compatibility Icons
- (:new_moon:) = Klipper or Voron specific.
- (:first_quarter_moon:) = Concept applies to all firmwares, but notable tips/commands/configs are Klipper or Voron specific.
- (:waxing_gibbous_moon:) = Applies to all firmwares, but some minor details (commands, configs) may differ (often noted).
- (:full_moon:) = Applies to printers, or all Marlin/Klipper printesr.

## **Before We Begin**
- [Before We Begin](/articles/before_we_begin.md)
    - **:warning: Important Checks**
- [A Note About Line Width](/articles/a_note_about_line_width.md)
- [Setting Expectations](/articles/setting_expectations.md)

## **Print Tuning** 
*Essentials. Read/follow these in order shown.*
- [Build Surface Adhesion](/articles/build_surface_adhesion.md) (:full_moon:)
- [First Layer Squish](/articles/first_layer_squish.md) (:waxing_gibbous_moon:)
- [Pressure Advance](/articles/pressure_advance.md) *("Linear Advance" in Marlin)* (:new_moon:)
    - Why PA is Needed
    - What PA Does
    - Pattern Method
    - Fine-Tuning and What to Look For
    - [Tower Method](/articles/pressure_advance_tower_method.md) (:new_moon:)
    - [Lines Method (DEPRECATED)](/articles/lines_method_deprecated.md) (:full_moon:)
- [Extrusion Multiplier](/articles/extrusion_multiplier.md) (:full_moon:)
    - Background 
    - Method
    - Rationale & Dimensional Accuracy
- [PA / EM Oddities](/articles/pa_em_oddities.md) (:waxing_gibbous_moon:)
    - Slight Perimeter Gapping
    - Slight Corner Gapping
- [Cooling and Layer Times](/articles/cooling_and_layer_times.md) (:full_moon:)
    - Signs of Overheating
    - How to Fix It
- [Retraction](/articles/retraction.md) (:full_moon:)
    - If You Are Having Persistent Issues
        - With PETG
- [Infill/Perimeter Overlap](/articles/infill_perimeter_overlap.md) (:full_moon:)

## **Printer Tuning**
*Mostly optional. For pushing limits, or for troubleshooting.\
"Voron V2 Gantry Squaring" is the only essential.*
- [Determining Maximum Volumetric Flow Rate](/articles/determining_max_volumetric_flow_rate.md) (:full_moon:)
    - Why?
    - Approximate Values
    - How Volumetric Flow Rate Relates to Print Speed
    - Formulas
    - Method
    - Flow Dropoff
- [Determining Motor Currents](/articles/determining_motor_currents.md) (:waxing_gibbous_moon:)
    - Determining Initial `run_current`
    - Determining Maximum `run_current`
    - Determining `hold_current`
- [Determining Maximum Speeds and Accelerations](/articles/determining_max_speeds_accels.md) (:new_moon:)
    - Method
    - Usage of the `TEST_SPEED` Macro
- [Voron V2 Gantry Squaring](/articles/voron_v2_gantry_squaring.md) (:new_moon:)

## **Miscellaneous**
- [Stepover](/articles/stepover.md) (:full_moon:) (The black magic secret for better overhangs)
- [Useful Macros](/macros/useful_macros.md) (:new_moon:)
    - Conditional Homing
    - Conditional QGL
    - :warning: Hotend Fan RPM Monitoring
    - My Pause/Resume Macros (For Runouts, Filament Swaps, and Manual Pauses)
        - Pause
        - Resume
        - Cancel
        - Octoprint Configuration 
        - M600 (Filament Change) Alias
        - Example Filament Sensor Config
            - Basic Filament Switch Sensor
            - Smart Filament Sensor
        - Filament Sensor Management
    - Beeper
    - LCD RGB
    - Parking
    - Off
    - Shut Down Pi
        - As option in LCD menu
    - Dump Variables
    - Get Variable
    - Replace `M109`/`M190` With `TEMPERATURE_WAIT`
- [Passing Slicer Variables to PRINT_START](/articles/passing_slicer_variables.md) (:new_moon:)
    - Passing Temperatures
        - SuperSlicer
        - Prusa Slicer
        - Cura
- [Controlling Slicer Temperature G-Code Order (Simple Method)](/articles/controlling_slicer_g-code_order.md) (:full_moon:)
- [My Setup](/articles/my_setup.md) (since people ask a lot)

## **Troubleshooting**
*Even without issues, you should look through these to familiarize yourself with things to look out for.\
**Especially** thermal drift under "First Layer / Squish Consistency Issues"*
### [Extrusion Patterns / "Wood Grain"](/articles/troubleshooting/extrusion_patterns.md)(:first_quarter_moon:)
- Extruder Backlash
- Other Factors
- Clockwork 1
- Mini Afterburner

![](/images/troubleshooting/Backlash-WoodGrain.png)

---
### [Bulging](/articles/troubleshooting/bulging.md) (:full_moon:)
- Bulging Layers
    - ![](/images/troubleshooting/Bulging.png) 

- Bulges at STL Vertices
    - ![](/images/troubleshooting/Vertex-Bulges.png) 

- Bulging around features (SS)
    - ![](/images/troubleshooting/bulging/feature_bulging.png) 

- Bulging Patterns on Overhangs (SS)
    - ![](/images/troubleshooting/AboveBridgeFlow-2.png)
---
### [Crimps](/articles/troubleshooting/crimps.md) (:full_moon:)
![](/images/troubleshooting/Microfit-Crimps.png)
---
### [Error: "Command Format Mismatch"](/articles/troubleshooting/command_format_mismatch.md) (:new_moon:)
---
### [Extruder Skipping](/articles/troubleshooting/extruder_skipping.md) (:first_quarter_moon:)
![](/images/troubleshooting/ExtruderSkips-2.png)
![](/images/troubleshooting/ExtruderSkips-5.png)
![](/images/pressure_advance/pa_lines_skipping.png)
---
### [First Layer / Squish Consistency Issues](/articles/troubleshooting/first_layer_squish_consistency.md) (:new_moon:)
- :warning:Thermal Drift
- First Layer Conistency
- Squish Consistency (Between Prints)

![](/images/FirstLayer-Squares-Textured.png)
---
### [Layer Shifting](/articles/troubleshooting/layer_shifting.md) (:first_quarter_moon:)
- Mechanical
- Electrical
- Speeds and Accelerations

![](/images/troubleshooting/LayerShifting/1.png)
---
### [Perimeter Separation](/articles/troubleshooting/perimeter_separation.md) (:full_moon:)
![](/images/troubleshooting/perimeter_separation/perimeter_separation.jpg)
---
### [PLA is Overheating](/articles/troubleshooting/pla_overheating.md) (:full_moon:)
---
### [Pockmarks](/articles/troubleshooting/pockmarks.md) (:full_moon:)
![](/images/troubleshooting/Pockmarks.png)
---
### [VFAs (Vertical Fine Artifacts)](/articles/troubleshooting/vfas.md) (:new_moon:)
- Repeating VFAs With ~2mm Spacing
- Repeating VFAs With Non-2mm Spacing

![](/images/troubleshooting/ToothMarks.png)
---
### [Slicer is Putting Heating G-codes in the Wrong Place/Order](/articles/troubleshooting/slicer_putting_heating_g-codes_wrong_order.md) (:first_quarter_moon:)
---
### [Small Infill Areas Look Overextruded](/articles/troubleshooting/small_infill_areas_overextruded.md) (:waxing_gibbous_moon:)
![](/images/troubleshooting/small_infill_overextruded/example1.png) 