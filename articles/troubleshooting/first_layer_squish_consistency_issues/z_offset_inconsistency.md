---
layout: default
title: Z Offset Inconsistency
nav_order: 3
parent: First Layer Inconsistencies
grand_parent: Troubleshooting
---
{% comment %} 
# This guide has moved! Please visit [the new site](https://ellis3dp.com/Print-Tuning-Guide/).
{% endcomment %}
# Z Offset Inconsistency
---
:dizzy: This page is tailored to **Voron** printers.

---

(If your Z offset seems to vary between prints.)

- Check your Z axis. Make sure everything is tight, especially grub screws.

- Ensure that everything is tight in your toolhead and across your X extrusion, including the hotend, nozzle, and probe.
- For **nozzle endstops**:
    - Ensure that your start g-code contains a final z homing **with a hot nozzle** near the end.

        - This ensures that any plastic remaining on the nozzle is squished out of the way, and is less likely to affect your Z offset.
        - This also accounts for the small amount of thermal expansion in the nozzle as it heats.
        - You can use a nozzle brush mod to automatically clean any debris. You should still home Z with a hot nozzle, though.
        - You can control when your heating occurs by [:page_facing_up: passing variables to `PRINT_START`.](../../passing_slicer_variables.md)

    - Ensure that the endstop pin is square on top, otherwise it can cause your Z offset to drift as it rotates over time.

        - Notching your Z endstop pin (as described in the Voron manuals) can prevent it from rotating.

    - Ensure that your nozzle is hitting the center of the pin.

    - Test your endstop's accuracy using [:page_facing_up: `PROBE_Z_ACCURACY`](https://github.com/protoloft/klipper_z_calibration#command-probe_z_accuracy). You may want to try different endstop switches to find a more accurate one.

        - **NOTE:** This *requires* you to install the above linked Klipper plug-in (klipper_z_calibration). This command is NOT built into Klipper natively. 

            - You can just install it for the accuracy test. You don't have to read/use anything else from that link.

            - Scroll all the way to the end of the main page for usage / arguments.

- For **V2**: 
    - **:warning: Ensure that you are homing Z again after QGL**, as QGL throws off Z height.
    - See the V2 notes under the [:page_facing_up: First Layer Consistency](./first_layer_inconsistency) page.

- For **inductive probes *as* Z endstop (virtual endstop)**:
    - Inductive probes thermally drift, meaning that your Z offset can change at different bed/enclosure temperatures. You may need to calibrate Z offset for the temperatures you intend to print at.
    
- For Klicky/Quickdraw [:page_facing_up: **Automatic Z Calibration***](https://github.com/protoloft/klipper_z_calibration):

    - Ensure that none of your magnets are loose.
        - If they are coming loose, make sure to lightly sand the tops of the magnets before gluing them back in. They adhere much better this way. Even still, I occasionally have one work its way loose.
    - Ensure that your `Calibrate_Z` macro is hitting the *body* of the Klicky microswitch on the Z endstop, not the *button* of the Klicky microswitch.
    - Try `PROBE_ACCURACY` and check how accurate your switch is. Sometimes you may need to try multiple switches to find the "best" one.

- See the [:page_facing_up: Thermal Drift](./thermal_drift.md) page. Ensure that you are heat soaking for long enough on larger enclosed printers.

<sup>\* This is a mod. It essentially baby steps for you, to account for different bed heights in addition to nozzle heights.</sup>