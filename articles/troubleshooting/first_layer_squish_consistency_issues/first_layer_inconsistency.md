---
layout: default
title: First Layer Inconsistency
nav_order: 2
parent: First Layer Inconsistencies
grand_parent: Troubleshooting
---
{% comment %} 
# This guide has moved! Please visit [the new site](https://andrewellis93.github.io/Print-Tuning-Guide/).
{% endcomment %}
# First Layer Inconsistency
---
:dizzy: This page is tailored to **Voron** / Klipper printers.

---
(If your squish seems to vary at different spots on the bed)

- In my opinion, you should use [:page_facing_up: bed mesh](https://docs.vorondesign.com/tuning/secondary_printer_tuning.html#bed-mesh). I personally recommend generating a bed mesh before every print, by adding `BED_MESH_CALIBRATE` to your `PRINT_START` macro. *(requires the config section in the link above.)*

    - With a physical Z endstop, make sure not omit the `relative_reference_index` setting described in the link above. Follow the formula. This setting is not needed when using the probe as your Z endstop (virtual endstop), however.
        - `relative_reference_index` = ((x points * y points) - 1) / 2

    - Use `algorithm: bicubic` instead of `algorithm: lagrange` when using a mesh size greater than 3x3.
    - Some discourage using bed mesh unless absolutely necessary, but I disagree. In my opinion it's cheap insurance. It's very rare for larger printers to have a perfect first layer without it.
    - **Your heat soaked mesh will be different from your cold mesh**. The bed and gantry can warp with heat. It will even vary at different temperatures. This is why I prefer to generate a fresh bed mesh for every print.

    - **Bed mesh can't always save you from mechanical problems.**
        - Most bed mesh issues are caused by the gantry rather than the bed itself.
            - For V2, follow my [:page_facing_up: V2 gantry squaring](../../voron_v2_gantry_squaring.md) instructions. A poorly squared gantry can be the root cause of a lot of first layer issues.
            - On all CoreXY printers: [:page_facing_up: de-rack](https://www.youtube.com/watch?v=cOn6u9kXvy0). 
                - For V2, this is part of the gantry squaring instructions above. Please follow those first/instead.
            - If you are using dual X rails, **make sure they are properly aligned with each other.** This can cause left-to-right first layer issues that mesh can't compensate for.
            - Ensure that everything is tight in your toolhead and across your X extrusion, including the hotend and nozzle.
    - Try more mesh points. Usually anything above 5x5 is overkill, but you can try up to 9x9.
        - With a physical Z endstop, don't forget to update your `relative_reference_index` when changing mesh points. This setting is not needed when using the probe as your Z endstop (virtual endstop), however.
            - `relative_reference_index` = ((x points * y points) - 1) / 2
- For **V2**:
    - Ensure that you place your `BED_MESH_CALIBRATE` **after** G32, as the stock G32 macro clears bed meshes.

    - You may need to play with how tight your bed mounting screws are.

        - I heat soak, fully hot-tighten 3/4 bed screws, and make the 4th screw "snug but not tight"
        
            - *It's commonly advised to mount your bed with only three screws, with "one tight, two loose". Anecdotally this advice has caused fist layer issues for me.*

    - Ensure that your Z belts are properly tensioned. They should all be roughly equal tensions. 
        - I tension mine to **140hz over a 150mm span** of belt.
            - Apps:
                - Android: Gates Carbon Drive (select "motorcyle" option) or Spectroid.
                - iPhone: Gates Carbon Drive (select "motorcyle" option) or Sound Spectrum Analysis.

        - Your closed loop belts (the short belts loops in the Z drive units) should be quite tight, but not so tight that they are pulling the motors shaft out of parallel. 
            - The stock tension levers don't always give enough tension on their own. You may have to loosen the motor mount, stick a flathead screwdriver between the lever tensioner and the Z drive main body to give it a bit more tension, and tighten it back down. 
            - (It's not easily possible to measure these with a frequency)

- For **V0**:
    - Ensure that your bed is solidly mounted. Check that the screws are not coming loose in the MGN7 carriage.

- For **inductive probes:**
    - Make sure your PEI is not bubbling in places. Inductive probes can only sense the subsurface, so cannot correct for PEI bubbles. 
    - Try leaving the toolhead sitting close to the center of the bed during your heat soak. Inductive probes thermally drift, and this can pre-heat it so that it does not drift *during* your mesh generation.
    - Microswitch-based magprobes (Klicky/Quickdraw) and other physical probes like BLTouch allow for detection of the actual print surface *(though I would recommend Klicky/Quickdraw over BLTouch if you take this route)*

- Ensure that there is no debris under your spring steel.
- Disable z lift (z hop) on first layer.

- Check your Z axis. Make sure everything is tight, especially grub screws.

- Run `PROBE_ACCURACY` to check for issues with your Z axis repeatability. 
    - My personal comfort zone:
        - Standard deviation ≤ **0.004**.
        - Range ≤ **0.0125**.
    - On **V2**, run `PROBE_ACCURACY` in each corner of the bed to check all four Z drives.

- Ensure that everything is tight in your toolhead and across your X extrusion, including the hotend, nozzle, and probe.

- See the [:page_facing_up: Thermal Drift](./thermal_drift.md) page. Ensure that you are heat soaking for long enough on larger enclosed printers.