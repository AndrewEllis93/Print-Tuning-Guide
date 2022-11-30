---
layout: default
title: Introduction
nav_order: 1
---

# Introduction

Some parts of this guide are tailored to printers running **Klipper**, but many pages work for other firmwares. See "Compatibility Icons" below.

This guide was originally written for the Voron community. Some notes and hardware troubleshooting tips are still Voron specific.
## Notes

- My SuperSlicer profiles are located [:page_facing_up: here](https://github.com/AndrewEllis93/Ellis-SuperSlicer-Profiles).
- If you have issues, comments, or suggestions about the guide, please let me know on GitHub issues or via Discord: [:page_facing_up: Ellis#4980](https://discordapp.com/users/207622442842062849)
    - For issues **not directly related to the guide content itself**, or for troubleshooting & print help, please use the public help channels in the [:page_facing_up: Voron Discord](https://discord.gg/voron) (or the appropriate community for your printer). 
- You can find the bed models and textures I am using [:page_facing_up: here](https://github.com/VoronDesign/Voron-Extras/tree/main/Bed_Models). The bed texture I am using in some of the older screenshots is from [:page_facing_up: VoronUsers.](https://github.com/VoronDesign/VoronUsers/tree/master/slicer_configurations/PrusaSlicer/hartk1213/V0/Bed_Shape) 
- Thank you to **bythorsthunder** for help with testing these methods and providing some of the photos.
- Support my drinking habits:
[![](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/paypalme/AndrewEllis93)
- Icons
    - :warning: = **:exclamation:Please pay extra attention to items marked with this.:exclamation:**
    - :page_facing_up: = Link to another page.
    - :pushpin: = Jump to section (on same page).


## Compatibility Icons
- (:new_moon:) = Klipper or Voron specific.
- (:first_quarter_moon:) = Concept applies to all firmwares, but notable tips/commands/configs are Klipper or Voron specific.
- (:waxing_gibbous_moon:) = Applies to all firmwares, but some minor details (commands, configs) may differ (often noted).
- (:full_moon:) = Applies to all printers, or all Marlin/Klipper printers.

---TODO--

## **Before We Begin**
- [Before We Begin](http://localhost:4000/Print-Tuning-Guide/articles/before_we_begin.html)
    - **:warning: Important Checks**
- [A Note About Line Width](http://localhost:4000/Print-Tuning-Guide/articles/a_note_about_line_width.html)
- [Setting Expectations](http://localhost:4000/Print-Tuning-Guide/articles/setting_expectations.html)

## **Print Tuning** 
*Essentials. Read/follow these in order shown.*
- [Build Surface Adhesion](http://localhost:4000/Print-Tuning-Guide/articles/build_surface_adhesion.html) (:full_moon:)
    - Build Surface Preparation / Handling
    - Troubleshooting
- [First Layer Squish](http://localhost:4000/Print-Tuning-Guide/articles/first_layer_squish.html) (:waxing_gibbous_moon:)
- [Pressure Advance / Linear Advance](http://localhost:4000/Print-Tuning-Guide/articles/pressure_advance.html) (:full_moon:)
    - Why PA is Needed
    - What PA Does
    - Pattern Method
    - Fine-Tuning and What to Look For
    - [Tower Method](http://localhost:4000/Print-Tuning-Guide/articles/pressure_advance_tower_method.html) (:new_moon:)
    - [Lines Method (DEPRECATED)](http://localhost:4000/Print-Tuning-Guide/articles/lines_method_deprecated.html) (:full_moon:)
- [Extrusion Multiplier](http://localhost:4000/Print-Tuning-Guide/articles/extrusion_multiplier.html) (:full_moon:)
    - Background 
    - Method
    - Rationale & Dimensional Accuracy
- [PA / EM Oddities](http://localhost:4000/Print-Tuning-Guide/articles/pa_em_oddities.html) (:waxing_gibbous_moon:)
    - Slight Perimeter Gapping
    - Slight Corner Gapping
- [Cooling and Layer Times](http://localhost:4000/Print-Tuning-Guide/articles/cooling_and_layer_times.html) (:full_moon:)
    - Signs of Overheating
    - How to Fix It
- [Retraction](http://localhost:4000/Print-Tuning-Guide/articles/retraction.html) (:full_moon:)
    - If You Are Having Persistent Issues
        - With PETG
- [Infill/Perimeter Overlap](http://localhost:4000/Print-Tuning-Guide/articles/infill_perimeter_overlap.html) (:full_moon:)

## **Printer Tuning**
*Mostly optional. For pushing limits, or for troubleshooting.\
"Voron V2 Gantry Squaring" is the only essential.*
- [Determining Maximum Volumetric Flow Rate](http://localhost:4000/Print-Tuning-Guide/articles/determining_max_volumetric_flow_rate.html) (:full_moon:)
    - Why?
    - Approximate Values
    - How Volumetric Flow Rate Relates to Print Speed
    - Formulas
    - Method
    - Flow Dropoff
- [Determining Motor Currents](http://localhost:4000/Print-Tuning-Guide/articles/determining_motor_currents.html) (:waxing_gibbous_moon:)
    - Determining Initial `run_current`
    - Determining Maximum `run_current`
    - Determining `hold_current`
- [Determining Maximum Speeds and Accelerations](http://localhost:4000/Print-Tuning-Guide/articles/determining_max_speeds_accels.html) (:new_moon:)
    - Method
    - Usage of the `TEST_SPEED` Macro
- [Voron V2 Gantry Squaring](http://localhost:4000/Print-Tuning-Guide/articles/voron_v2_gantry_squaring.html) (:new_moon:)

## **Miscellaneous**
- [Stepover](http://localhost:4000/Print-Tuning-Guide/articles/stepover.html) (:full_moon:) (The black magic secret for better overhangs)
- [Useful Macros](/macros/useful_macros.html) (:new_moon:)
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
- [Passing Slicer Variables to PRINT_START](http://localhost:4000/Print-Tuning-Guide/articles/passing_slicer_variables.html) (:new_moon:)
    - Passing Temperatures
        - SuperSlicer
        - Prusa Slicer
        - Cura
- [Controlling Slicer Temperature G-Code Order (Simple Method)](http://localhost:4000/Print-Tuning-Guide/articles/controlling_slicer_g-code_order.html) (:full_moon:)
- [My Setup](http://localhost:4000/Print-Tuning-Guide/articles/my_setup.html) (since people ask a lot)

