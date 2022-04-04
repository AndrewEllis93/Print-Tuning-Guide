# First Layer Squish

I'm going to call it "squish" to be unambiguous. "Z offset" and "z height" can be conflated with other concepts. 

- **:warning:** This section assumes that you have already done a rough [:page_facing_up:Z offset calibration](https://docs.vorondesign.com/build/startup/#initial--simple-process).

- **:warning:** This section also assumes that you have a *consistent* first layer squish, both across the entire build surface and between prints. 
    - **:warning:** See the [:page_facing_up:First Layer / Squish Consistency Issues](/articles/troubleshooting/first_layer_squish_consistency.md) article, **even if you are not having any issues.** There is some important information in there that everyone should know, particularly about **thermal drift**.
## Method
**1)** Scatter square patches around your bed in your slicer. 
- See the *test_prints* folder. Choose a patch that matches your first layer height.
- ![](/images/FirstLayer-Plate.png)    

**2)** Set your first layer height to **0.25** or greater.

- Thinner first layer heights are considerably more sensitive and more difficult to maintain.

**3)** Set your first layer [:page_facing_up:line width](/articles/before_we_begin.md#a-note-about-line-width) to **120%** or greater.

**4)** Start the print. While it is printing, [:page_facing_up:live adjust z](https://docs.vorondesign.com/build/startup/#fine-tuning-z-height).

- This can be done via g-codes/macros, LCD, or via web. I find it easiest to sit in front of the printer and fine-tune with the LCD.
### Examples
In these examples, the third square is closest.\
There are print examples in the next section.

Note: When I refer to "gaps", I mean where you can see BETWEEN/THROUGH the extrusion lines. If you can see any light (excluding pinholes at the perimeter), or the next layer, then you need more squish.
- #### Smooth Build Surface
    - **Top Surface**
        - You don't want too many ridges/hairs on top. 
            - It's normal to have a *little* bit of this near the corners, or in small  footprint areas.
        - You shouldn't see any gaps* between the lines.
            - It's fine to have some very small pinholes where the infill meets the     perimeters.
        - ![](/images/FirstLayer-Squares-2.png)
        - ![](/images/FirstLayer-Squares-2-Annotated.png)
    - **Bottom Surface**
        - You should not have any gaps between the lines.
        - You should still be able to clearly see the lines. They should not be fading or   invisible.
        - ![](/images/FirstLayer-Squares-1-Annotated.png)
- #### Textured Build Surface
    - **Top Surface**
        - Follow the same guidance as for smooth build surfaces (above). You can see hairs/lumps with too much squish, and gaps with not enough squish.
        - ![](/images/FirstLayer-Squares-Textured.png)
    - **Bottom Surface**
        - **The lines will not be as visible as on a smooth build surface.**
        - As with smooth build surfaces, you should not have any gaps between the lines.
        - With textured, it's a bit easier to tell squish using the top surface rather than the bottom surface.
        - ![](/images/FirstLayer-Squares-Textured-2.jpg)

**5)** Once you are happy with your squish, cancel the print and then save your new offset with one of the below methods:

- **Dedicated Z Endstop:**\
(With dedicated Z endstops. Stock V0/V2/Trident are set up this way)
    - Enter `Z_OFFSET_APPLY_ENDSTOP`* 
        - This will apply your new offset to your stepper_z's `position_endstop`.
    - Enter `SAVE_CONFIG`.

- **Virtual Z Endstop:**\
(When using the probe *as* the Z endstop. Stock Switchwire and Legacy are set up this way)
    - Enter `Z_OFFSET_APPLY_PROBE`*
        - This will apply your new offset to your probe's `z_offset`.
    - Enter `SAVE_CONFIG`.

- **Klicky Auto Z Calibration:**\
(This is a mod, it uses Klicky AND nozzle endstop to automatically baby step before each print. See [:page_facing_up:here](https://github.com/protoloft/klipper_z_calibration) for more information.)
    - Manually adjust your `switch_offset` based on how much extra you had to baby step. 
        - Higher value = more squish 
        - Lower value = less squish

<sup>* Requires a semi-recent version of Klipper.</sup>
## Print Examples 
You should still clearly be able to see the lines. If it's completely smooth, your squish is too much.
 If you see gaps between the lines, you need more squish.
### Good Squish
- ![](/images/FirstLayer-PrintExample.jpg) 


### Too Much Squish

- Can't see any lines, or the lines are starting to fade (smooth PEI):

    - ![](/images/FirstLayer-TooMuchSquish2.png) ![](/images/FirstLayer-TooMuchSquish1.png) 

- Wavy patterns appear:

    - ![](/images/FirstLayer-TooMuchSquish3.png) ![](/images/FirstLayer-TooMuchSquish4.png) 


### Not Enough Squish
- There are gaps between the lines (you can see through to the next layer):

    - ![](/images/FirstLayer-NotEnoughSquish1.png) ![](/images/FirstLayer-NotEnoughSquish2.png) ![](/images/FirstLayer-NotEnoughSquish3.png) 

    ## Close, But Not Quite
    - This cube needs just a tiny bit more squish.\
    You can see very slight gapping / shadows between the perimeters and some areas of the infill. The corners are also starting to pull away a bit.
    ![](/images/FirstLayer-NotEnoughSquish4.png)
    - Better!\
        ![](/images/FirstLayer-NotEnoughSquish4-Better.png)
