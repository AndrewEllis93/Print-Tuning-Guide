[:arrow_left: Back to Table of Contents](/README.md)

---
# Perimeter Separation

Adapted from [**bythorsthunder**](https://discordapp.com/users/830305218679144509)'s Discord pin. Thanks!

![](/images/troubleshooting/perimeter_separation/perimeter_separation.jpg)


## If It Happens Primarily on Lower Layers

- Ensure you have enough first layer squish. See [:page_facing_up:here.](/articles/first_layer_squish.md) 
- Check your elephant's foot / first layer compensation settings. 
    - Reduce the amount, disable it, or fade it (SS only).
    - Having this set too high (especially when combined with bottom chamfers) can cause perimeters to **print over nothing.**
        - **Too high:**\
        ![](/images/troubleshooting/perimeter_separation/comp_on.png)
        - **Off:**\
        ![](/images/troubleshooting/perimeter_separation/comp_off.png)
    - **SuperSlicer:** "XY first layer compensation" (`first_layer_size_compensation`)
        - You can also increase `first_layer_size_compensation_layers`, which gradually fades the compensation out over X number of layers.
    - **Prusa Slicer:** "Elephant foot compensation" (`elefant_foot_compensation` - yes it's misspelled)
    - **Cura:** "Initial layer horizontal expansion"

## If It Happens Everywhere
- Increase your external perimeter line width*. 
    - This provides more overlap with the previous layer. See [:page_facing_up:stepover](/articles/stepover.md).
    - \* *Unless you are printing Voron parts - they are designed for 0.4mm external perimeter widths.*
- Verify your extrusion multiplier. There should be no gaps or holes in top solid surfaces. See [:page_facing_up:here](/articles/extrusion_multiplier.md).
- Try decreasing your perimeter speed.  
    - If it only affects holes, you can slow them down in PS/SS by lowering `small_perimeter_speed`.
        - In SS, you can configure small perimeter size thresholds using `small_perimeter_min_length`/`small_perimeter_max_length`. 
    - Use the speed preview to ensure that it's activating where you want it to.
- Try increasing your hotend temperature. This helps with layer bonding strength.
    - High speed printing often needs a temperature bump. ABS is usually in the 240-255 range.
- Make sure you are not printing external perimeters first.
---

[:arrow_left: Back to Table of Contents](/README.md)