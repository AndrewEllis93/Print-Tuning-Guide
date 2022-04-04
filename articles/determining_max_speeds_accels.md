# Determining Maximum Speeds and Accelerations

This article is purely about finding your absolute maximum speeds/accels. **This does not necessarily mean that these speeds or accelerations will be practical to print with** - but it can be handy to find the limits of your printer. You can use max speeds for things like travels, mesh, QGL, etc.

You may be able to get higher performance out of your motors by increasing currents (see previous section), but be careful not to push them too high.

**You may also get higher maximum accelerations by utilizing input shaper, and may want to re-tune your max accels after tuning input shaper.**

1.8° motors can generally reach higher top speeds/accels than 0.9° motors. Higher voltage systems (e.g. 24v vs 12v) can also generally reach higher top speeds/accels.

For example my 2a 0.9° LDO motors top out around 450mm/s. My 2a 1.8° OMC motors topped out closer to 700-800mm/s.
## Method

Tune maximum speeds first, THEN tune accelerations separately.

**1)** Add [:page_facing_up:this macro](/macros/TEST_SPEED.cfg) to your `printer.cfg` file.

**2)** If you are already pushing high accels, then lower your `max_accel` in your config to something closer to "stock" and `reload`. 
- Reference the stock Voron configs for a reasonable starting point.
    - Some wild guesses:
        - Linear rail CoreXY: *3000mm/s²*
        - Linear rod CoreXY: *2000mm/s²*
        - Bed slinger: *1000mm/s²* 
- `max_accel` needs to be high enough to actually *reach* full speed in a given print volume, but low enough to not risk causing skipping on its own. **This is purely to isolate variables.** You will come back and tune actual max accels later *(step 8)*.
- You can use the "acceleration" graphing calculator at the bottom of the page [:page_facing_up:here](https://blog.prusaprinters.org/calculator_3416/) to verify that you will be reaching max speed.
    - For example, for a 300mm linear rail CoreXY printer:
        - Note that the test pattern is **inset 20mm by default** (to help avoid collisions). Hence the distance of **260mm** *(300-20\*2)*.
        - The **blue line** shows that a max speed of 500mm/s is actually being reached and maintained.
        - ![](/images/TEST_SPEED_Calc.png) 
        - This graph also shows (the **yellow line**) that we would max out a bit under **900mm/s** at this acceleration/distance.


**3)** Run the `TEST_SPEED` macro using the [:pushpin:instructions below](/articles/determining_max_speeds_accels.md#usage-of-the-test_speed-macro) with increasing speeds [:pushpin:until you experience skipping.](#determining-if-skipping-occured) 
- Start with a small number of iterations.
    - Example: `TEST_SPEED SPEED=350 ITERATIONS=2`
- Once you experience skipping, back the speed down and try again until you no longer get any skipping.

**4)** Once you have found a rough maximum, run the test again with a large number of iterations.
- This is essentially an extended torture test.
    - Example: `TEST_SPEED SPEED=400 ITERATIONS=50`
- If you experience any skipping during extended tests, back the speed down again.

**5)** *Use a slightly lower value than your results.*
- Sometimes a maximum that works perfectly, even in extended torture tests, can skip during actual prints. Go a bit lower for a margin of safety.

**6)** Save your new maximum velocity to `max_velocity` in your config.

**7)** Return your `max_accel` in your config to its previous value. *(changed in step 2)* and then `reload`.

**8)** Repeat the process, this time increasing accelerations rather than speeds.
- Example: `TEST_SPEED ACCEL=400 ITERATIONS=2`

**9)** Save your new maximum acceleration to `max_accel` in your config and `reload`.
- Set your `max_accel_to_decel` to *half* of this value.

## Usage of the TEST_SPEED Macro

The macro is available [:page_facing_up:here.](Macros/TEST_SPEED.cfg)

This macro will home, QGL *(if your printer uses QGL / has not yet done a QGL)*, move the toolhead in a test pattern at the specificed speeds/accels, and home again. 

You will [:pushpin:watch, listen, and compare the terminal output from before/after.](#determining-if-skipping-occured)

### Available arguments (omitting any will use the default value)
- `SPEED` - Speed in mm/sec. 
    - *Default: your `max_velocity`*
- `ACCEL` - Acceleration in mm/sec².
    - *Default: your `max_accel`*
- `ITERATIONS` - Number of times to repeat the test pattern 
    - *Default: 5*
- `BOUND` -  (Normally you do not need to specify/change this) How far to inset the "large" test pattern from the edges (in mm).This just helps prevent slamming the toolhead into the sides after small skips, and also accounts for imperfectly set printer dimensions.
    - *Default: 20*
- `SMALLPATTERNSIZE` -  (Normally you do not need to specify/change this) The box size of the "small" movement pattern to perform at the center (in mm).
    - *Default: 20*

**:warning:** *Note that any speed or acceleration you input into this macro can **exceed** 
`max_velocity` and `max_accel` from your config. 
### Examples

- `TEST_SPEED SPEED=350 ITERATIONS=50` 

- `TEST_SPEED ACCEL=10000 ITERATIONS=50` 

### Determining if Skipping Occured

**1.** Watch and listen. 
- Often, the skipping will be very obvious. Your toolhead may start shuddering and making erratic movements and loud noises.
- **Even if no skipping occurs, your motors might start to make loud resonant noises.** This can be an indication that you are near the limit, and should consider backing off a bit.

**2.** If there was no apparent major skipping, check for minor skipping:

- Inspect the g-code terminal output:
    - Compare the numbers for the X and Y steppers for the first and second homing.
    - ![](/images/TEST_SPEED_Compare.png) 
    - These numbers represent the microstep position of the toolhead at X/Y max position.
    - Ensure that the difference between these numbers **has not exceeded a full step.**
        - For example, I am running `microsteps` of **32** for my A and B motors. I would ensure that the values for each axis have not changed by more than **32**.
        - If the number has deviated more than this, that means that the corresponding axis has likely skipped.

    \* *Measuring to a full step just accounts for endstop variance. It does not necessarily mean that any microsteps were lost. Endstops are only so accurate.*