[:arrow_left: Back to Table of Contents](/README.md)

---
# First Layer / Squish Consistency Issues
## Thermal Drift

(This can affect first layer consistency *and* z offset consistency between prints.)

- **:warning: On larger enclosed printers (i.e. V2 & Trident), ensure that you are heat soaking for *at least* an hour.** \
\
Z will drift upwards as the frame and gantry thermally expand with chamber heat. This can cause your first layer squish to vary between prints, and can even cause your first layer to drift up *as it prints*.

    Don't believe me? Look at this. The red line represents Z offset drift over time, as the frame comes up to temperature.

    ![](/images/ZDrift.png)

    It's not ideal, but just get into a routine - start the heat soak from your phone when you wake up in the morning.\
    There *are* ways around this - specifically by using gantry backers in combination with software-based frame thermal expansion compensation, but that is a rabbit hole well outside the scope of this guide.* 
    
    <sup>* *Some links: :page_facing_up:[1](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/whoppingpochard/extrusion_backers) [2](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/bythorsthunder/MGN9_Backers) [3](https://deepfriedhero.in/products/titanium-extrusion-backers?_pos=1&_sid=e2f989fec&_ss=r) [4](https://www.fabreeko.com/collections/voron/products/v2-4-trident-titanium-extrusion-backers) [5](https://github.com/tanaes/whopping_Voron_mods/blob/main/docs/frame_expansion/frame_thermal_compensation_howto.md) [6](https://github.com/alchemyEngine/measure_thermal_behavior) [7](https://github.com/alchemyEngine/measure_thermal_behavior/blob/main/process_frame_expansion.py) [8](https://youtu.be/RXJKdh1KZ0w)</sup>*\
    <sup>\* *This is the one thing I would ask you not to message me about. It is outside the scope of what I am hoping to accomplish with this guide. The graph above is solely intended to demonstrate my point about heat soak times.*</sup>

## First Layer Consistency
(If your squish seems to vary at different spots on the bed)

- In my opinion, you should use [:page_facing_up:bed mesh](https://docs.vorondesign.com/tuning/secondary_printer_tuning.html#bed-mesh). I personally recommend generating a bed mesh before every print, by adding `BED_MESH_CALIBRATE` to your `PRINT_START` macro. *(requires the config section in the link above.)*

    - With a physical Z endstop, make sure not omit the `relative_reference_index` setting described in the link above. Follow the formula. This setting is not needed when using the probe as your Z endstop (virtual endstop), however.
        - `relative_reference_index` = ((x points * y points) - 1) / 2

    - Use `algorithm: bicubic` instead of `algorithm: lagrange` when using a mesh size greater than 3x3.
    - Some discourage using bed mesh unless absolutely necessary, but I disagree. In my opinion it's cheap insurance. It's very rare for larger printers to have a perfect first layer without it.
    - **Your heat soaked mesh will be different from your cold mesh**. The bed and gantry can warp with heat. It will even vary at different temperatures. This is why I prefer to generate a fresh bed mesh for every print.

    - **Bed mesh can't always save you from mechanical problems.**
        - Most bed mesh issues are caused by the gantry rather than the bed itself.
            - For V2, follow my [:page_facing_up:V2 gantry squaring](/articles/voron_v2_gantry_squaring.md) instructions. A poorly squared gantry can be the root cause of a lot of first layer issues.
            - On all CoreXY printers: [:page_facing_up:de-rack](https://www.youtube.com/watch?v=cOn6u9kXvy0). 
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

- See the [:pushpin:Thermal Drift](/articles/troubleshooting/first_layer_squish_consistency.md#thermal-drift) section. Ensure that you are heat soaking for long enough on larger enclosed printers.
## Squish Consistency (Between Prints)

(If your Z offset seems to vary between prints.)

- Check your Z axis. Make sure everything is tight, especially grub screws.

- Ensure that everything is tight in your toolhead and across your X extrusion, including the hotend, nozzle, and probe.
- For **nozzle endstops**:
    - Ensure that your start g-code contains a final z homing **with a hot nozzle** near the end.

        - This ensures that any plastic remaining on the nozzle is squished out of the way, and is less likely to affect your Z offset.
        - This also accounts for the small amount of thermal expansion in the nozzle as it heats.
        - You can use a nozzle brush mod to automatically clean any debris. You should still home Z with a hot nozzle, though.
        - You can control when your heating occurs by [:page_facing_up:passing variables to `PRINT_START`.](/articles/passing_slicer_variables.md)

    - Ensure that the endstop pin is square on top, otherwise it can cause your Z offset to drift as it rotates over time.

        - Notching your Z endstop pin (as described in the Voron manuals) can prevent it from rotating.

    - Ensure that your nozzle is hitting the center of the pin.

    - Test your endstop's accuracy using [:page_facing_up:`PROBE_Z_ACCURACY`](https://github.com/protoloft/klipper_z_calibration#command-probe_z_accuracy). You may want to try different endstop switches to find a more accurate one.

        - **NOTE:** This *requires* you to install the above linked Klipper plug-in (klipper_z_calibration). This command is NOT built into Klipper natively. 

            - You can just install it for the accuracy test. You don't have to read/use anything else from that link.

            - Scroll all the way to the end of the main page for usage / arguments.

- For **V2**: 
    - **:warning: Ensure that you are homing Z again after QGL**, as QGL throws off Z height.
    - See the V2 notes under the [:pushpin:First Layer Consistency section](/articles/troubleshooting/first_layer_squish_consistency.md#first-layer-consistency) above.

- For **inductive probes *as* Z endstop (virtual endstop)**:
    - Inductive probes thermally drift, meaning that your Z offset can change at different bed/enclosure temperatures. You may need to calibrate Z offset for the temperatures you intend to print at.
    
- For Klicky/Quickdraw [:page_facing_up:**Automatic Z Calibration***](https://github.com/protoloft/klipper_z_calibration):

    - Ensure that none of your magnets are loose.
        - If they are coming loose, make sure to lightly sand the tops of the magnets before gluing them back in. They adhere much better this way. Even still, I occasionally have one work its way loose.
    - Ensure that your `Calibrate_Z` macro is hitting the *body* of the Klicky microswitch on the Z endstop, not the *button* of the Klicky microswitch.
    - Try `PROBE_ACCURACY` and check how accurate your switch is. Sometimes you may need to try multiple switches to find the "best" one.

- See the [:pushpin:Thermal Drift](/articles/troubleshooting/first_layer_squish_consistency.md#thermal-drift) section. Ensure that you are heat soaking for long enough on larger enclosed printers.

<sup>\* This is a mod. It essentially baby steps for you, to account for different bed heights in addition to nozzle heights.</sup>

---

[:arrow_left: Back to Table of Contents](/README.md)