# First Layer / Squish Consistency Issues
### Thermal Drift

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

### First Layer Consistency
(If your squish seems to vary at different spots on the bed)

- In my opinion, you should use [:page_facing_up:bed mesh](https://docs.vorondesign.com/tuning/secondary_printer_tuning.html#bed-mesh). I personally recommend generating a bed mesh before every print, by adding `BED_MESH_CALIBRATE` to your `PRINT_START` macro. *(requires the config section in the link above.)*
    - Do not omit the `relative_reference_index` setting described in the link above. Follow the formula.
    - Use `algorithm: bicubic` instead of `algorithm: lagrange`.
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
        - Don't forget to update your `relative_reference_index` when changing mesh points.
- For **V2**:
    - Ensure that you place your `BED_MESH_CALIBRATE` **after** G32, as the stock G32 macro clears bed meshes.
    - You may need to play with how tight your bed mounting screws are. 
        - The common advice of only three bed screws, with "one tight, two snug" is generally good advice. 
        - I've found that if any are *too* loose, it can cause first layer consistency issues.
    - Ensure that your Z belts are properly tensioned. They should all be roughly equal tensions. 
        - I tension mine to **140hz over a 150mm span** of belt.
        - Your closed loop belts (the short belts loops in the Z drive units) should be quite tight, but not so tight that they are pulling the motors shaft out of parallel. 
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
### Squish Consistency (Between Prints)

(If your Z offset seems to vary between prints.)

- Check your Z axis. Make sure everything is tight, especially grub screws.
- Ensure that everything is tight in your toolhead and across your X extrusion, including the hotend, nozzle, and probe.
- For **nozzle endstops**:
    - Ensure that your start g-code contains a final z homing **with a hot nozzle** near the end.
        - This ensures that any plastic remaining on the nozzle is squished out of the way, and is less likely to affect your Z offset.
        - This also accounts for the small amount of thermal expansion in the nozzle as it heats.
        - You can use a nozzle brush mod to automatically clean any debris. You should still home Z with a hot nozzle, though.
    - Ensure that the endstop pin is square on top, otherwise it can cause your Z offset to drift as it rotates over time.
        - Notching your Z endstop pin (as described in the Voron manuals) can prevent it from rotating.
    - Ensure that your nozzle is hitting the center of the pin.

- For **V2**: 
    - **:warning: Ensure that you are homing Z again after QGL**, as QGL throws off Z height.
    - See the above V2 section.

- For **inductive probes *as* Z endstop (virtual endstop)**:
    - Inductive probes thermally drift, meaning that your Z offset can change at different bed/enclosure temperatures. You may need to calibrate Z offset for the termperatures you intend to print at.
    
- For Klicky/Quickdraw [:page_facing_up:**Automatic Z Calibration***](https://github.com/protoloft/klipper_z_calibration):

    - Ensure that none of your magnets are loose.
        - If they are coming loose, make sure to lightly sand the tops of the magnets before gluing them back in. They adhere much better this way.
    - Ensure that your `Calibrate_Z` macro is hitting the *body* of the Klicky switch on the Z endstop, *not* the button of the Klicky switch.
    - Try `PROBE_ACCURACY` and check how accurate your switch is. Sometimes you may need to try multiple switches to find the "best" one.

- See the [:pushpin:Thermal Drift](/articles/troubleshooting/first_layer_squish_consistency.md#thermal-drift) section. Ensure that you are heat soaking for long enough on larger enclosed printers.

<sup>\* This is a mod. It essentially baby steps for you, to account for different bed heights in addition to nozzle heights.</sup>
