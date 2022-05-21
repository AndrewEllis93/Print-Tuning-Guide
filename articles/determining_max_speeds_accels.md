[:arrow_left: Back to Table of Contents](/README.md)
# Determining Maximum Speeds and Accelerations

This article is purely about finding your absolute maximum speeds/accels. **This does not necessarily mean that these speeds or accelerations will be practical to print with,** and in fact your max speeds/accels will often be way higher than is reasonable to daily drive (for longevity). 

It's very handy for troubleshooting motor skipping issues, and for optimizing 0.9° motors, however. You can also use these speeds for travels (but fast travels have significantly dimishing returns for overall print times). Or just if you're into speed benchies.

It's also just a bit of fun. <sup>haha printer go brrrr</sup>

**Notes:**

- 1.8° motors can generally reach higher top speeds/accels than 0.9° motors. 

    - For example my 2a 0.9° LDO motors top out around 450mm/s. My 2a 1.8° OMC motors could reach closer to 800-1000mm/s.

- You may be able to get higher performance out of your motors by increasing currents (see [:page_facing_up:here](/articles/determining_motor_currents.md) for more info), but be careful not to push them too high.

- You may also get higher maximum accelerations by utilizing input shaper, and may want to **re-tune your max accels after tuning input shaper.**

- Higher voltage systems (e.g. 24v vs 12v) can also generally reach higher top speeds/accels.

## Method

Tune maximum accelerations first, THEN tune speeds second.

Note: input shaper will affect these values. You may need to run through this again if you enable or disable input shaper.

**1)** Add [:page_facing_up:this macro](/macros/TEST_SPEED.cfg) to your `printer.cfg` file.

**2)** If you are have increased your `max_velocity`, lower it back to the original value (check the stock configs for your printer) and `RELOAD`. 

**3)** Fully heat soak your printer. 
- Ideally the test should be run at the same chamber temps as your actual printing conditions.

**4)** Run the `TEST_SPEED` macro using the [:pushpin:instructions below](/articles/determining_max_speeds_accels.md#usage-of-the-test_speed-macro) with increasing accelerations [:pushpin:until you experience skipping.](#determining-if-skipping-occured) 
- Start with a small number of iterations.
    - Example: `TEST_SPEED ACCEL=5000 ITERATIONS=2`

- Once you experience skipping, back the acceleration down and try again until you no longer get any skipping.

**5)** Once you have found a rough maximum, run the test again with a large number of iterations.

- This is essentially an extended torture test.
    - Example: `TEST_SPEED ACCEL=5000 ITERATIONS=50`

- If you experience any skipping during extended tests, back the speed down again.

**6)** *Use a slightly lower value than your results.*
- Sometimes a maximum that works perfectly, even in extended torture tests, can skip during actual prints. Go a bit lower for a margin of safety.

**7)** Save your new maximum acceleration to `max_accel` in your config and `RELOAD`.
- Set your `max_accel_to_decel` to *half* of this value.

**8)** Use the "acceleration" graphing calculator at the bottom of the page [:page_facing_up:here](https://blog.prusaprinters.org/calculator_3416/) to find the theoretical maximum speed for your acceleration/print area. Remember it for the next step.

- This is only a *theoretical* maximum. I will explain more in the next step.

- For example, for a 300mm printer*, with a max accel of 3500:

    - \* Note that the test pattern is **inset 20mm by default** to help avoid collisions. Hence the distance of **260mm** *(300-20\*2)*.

    - The "desired speed" field is arbitrary for our purposes. Enter anything or use the default.

    - This **yellow line** shows that we would theoretically max out a bit over **900mm/s** at this acceleration/distance.
    - ![](/images/TEST_SPEED_Calc.png) 

    
        - The **blue line** just shows how far a given speed would be maintained (400mm/s in this example - arbitrarily chosen)

**8)** Repeat the process (steps 1-6), this time increasing speeds rather than accelerations. 
- Keep in mind that you can **only go up to the theoretical maximum value you found in the previous step.**
    - In most cases, this is very high and a non-issue. 

    - In some cases, however, you may be wondering why you can achieve seemingly "infinite" speeds. This probably means that your printer is not actually able to reach the requested speed at that accel/distance!

- Once again, run an extended "torture test" once you find your rough limit. 
- Example: `TEST_SPEED SPEED=450 ITERATIONS=50`

**9)** Save your new maximum speed to `max_velocity` in your config and `RELOAD`.
## Usage of the TEST_SPEED Macro

The macro is available [:page_facing_up:here.](/macros/TEST_SPEED.cfg)

This macro will home, QGL*, move the toolhead in a test pattern at the specificed speeds/accels, and home again. 
- **If your printer uses QGL / has not yet done a QGL. This is important, as a contorted gantry can cause alignment issues and skipping.*

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

**:warning:** Note that any speeds/accels you input into this macro can **override** the `max_velocity` and `max_accel` from your config. 
### Examples

- `TEST_SPEED SPEED=400 ITERATIONS=50` 

- `TEST_SPEED ACCEL=10000 ITERATIONS=50` 

### Determining if Skipping Occured

**1.** Watch and listen. 
- Often, the skipping will be very obvious. Your toolhead may start shuddering and making erratic movements and loud noises.

**2.** If there was no apparent major skipping, check for minor skipping:

- Inspect the g-code terminal output:
    - Compare the numbers for the X and Y steppers for the first and second homing.
    - ![](/images/TEST_SPEED_Compare.png) 
        - These numbers represent the microstep position of the toolhead at X/Y max position.

    - Ensure that the difference between these numbers **has not exceeded a full step.**
        - For example, I am running `microsteps` of **32** for my A and B motors. I would ensure that the values for each axis have not changed by more than **32**.
        - If the number has deviated more than this, that means that the corresponding axis has likely skipped.

    \* *Measuring to a full step just accounts for endstop variance. It does not necessarily mean that any microsteps were lost. Endstops are only so accurate.*