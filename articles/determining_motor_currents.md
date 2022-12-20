---
layout: default
title: Determining Motor Currents
nav_order: 2
parent: Advanced Tuning
---
{% comment %} 
# This page has moved! Please visit [the new location](https://ellis3dp.com/Print-Tuning-Guide/articles/determining_motor_currents.html).
{% endcomment %}
# Determining Motor Currents
{: .no_toc }

---

{: .compat}
:dizzy: This page is compatible with **Klipper only**.

---
<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---
:warning: The below guidance is for **axis motors only**.

Extruder motors/pancake steppers are a bit different, as there is more variance between models.

- **Check with the community first.**
    - If you are using BoM motors, check the stock configs.

    - Check in Discord to see what others are running.

- **You should start off with a more conservative** `run_current`.
    - You may be able to attain additional motor performance by increasing currents, but come back to that later. **Get your printer working reliably first.**

- **Some motors vary.**
    - I have found my LDO 0.9° steppers to be able to achieve notably higher max accels/speeds with higher currents. 

    - My OMC 1.8° motors, on the other hand, performed very well even at moderate currents.

- **Different stepper drivers have different maximum currents**.
    - See [:page_facing_up: here](https://learn.watterott.com/silentstepstick/comparison/). Try not to exceed ~70-80% of the rated maximum of your drivers (and remember that higher currents need more stepper driver cooling).

        - For example TMC2209 drivers are rated to 2a RMS, but I would generally not exceed 1.4a RMS.

- We are derating the motors/drivers for margin of safety. 
    - Rated currents are the absolute maximum *in ideal conditions*. In reality, things like chamber and driver temperature come into play. Margin of safety is also standard practice.


## Determining Initial `run_current`:
Start with around **40-50%** of rated current.

- For example, with a 2a motor, start around 0.8-1a.

Then you can [:page_facing_up: test your maximum speeds/accels](./determining_max_speeds_accels.md) and make sure your motors are performing well. In most cases, the motors can handle speeds/accels much faster than what you would realistically be printing at, even at moderate currents.
- If you are having issues reaching reasonable speeds/accels, you may have a mechanical problem. See [:page_facing_up: here](./troubleshooting/layer_shifting.md).

## Determining Maximum `run_current`:

---------------------------------
:warning: **In most cases, your motors will reach maximum or near-maximum performance before this point. Don't just slap them straight to max current.** 

- Often that just results in extra heat (and potential driver overheating problems) for little actual gain past a certain breakpoint.

- Most 1.8° motors already have way more performance than you realistically need. 0.9° motors are more sensitive, however.

- The ideal current is usually somewhere in the middle. Experiment with different motor currents and [:page_facing_up: test how they affect your maximum speeds/accels](./determining_max_speeds_accels.md).

---------------------------------

A good rule of thumb is to not exceed **70%** of the rated current as absolute max.

For example, a 2a motor would be about 1.4a max.


- Keep in mind that currents approaching maximum may need greater stepper driver cooling.

- If you are pushing higher currents, you may also want to consider measuring the temperature of your motors. Ensure that they do not exceed 80C.
    - Measure the temps when actually printing in a heat soaked chamber.
        - Some multimeters come with a k-type thermocouple. You can kapton tape it to the motor housing.
    - *You cannot accurately gauge this by feel.* Even lower temperatures will feel "too hot".
    - The motors themselves can generally handle much more. This temp limit comes from the printed parts rather than the motors themselves.
    
## Determining `hold_current`
Recently, Klipper docs have started to [:page_facing_up: recommend against using a separate `hold_current`.](https://github.com/Klipper3d/klipper/pull/4977) You can achieve this by commenting out `hold_current`, or by setting it to the same value as your `run_current`.

If you run a different `hold_current`, a good rule of thumb is about 70% of your `run_current`.

