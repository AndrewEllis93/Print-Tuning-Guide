# Retraction

**:warning: You should [:page_facing_up:tune pressure advance](/articles/pressure_advance.md) first.**
Pressure advance can lower the amount of retraction needed, especially for bowden.

If you typically print with z-hop, leave it on for this test.*\
<sup>\* Don't go overboard or it will cause more stringing. 0.2mm-0.3mm is usually enough.</sup>

**There is some trial and error involved.** You may need to re-run these tests at varying retraction speeds and temperatures if you are not getting good results. You will just have to experiment. You should hot tighten your nozzle (unless it's an E3D Revo).

If you are having persistent issues:
- **:warning: Ensure that your filament is dry.** Wet filament can cause near-unfixable stringing.
- Ensure that your hotend is not leaking around the threads or heat break. This can indicate that your nozzle or heatbreak is loose or not making adequate contact.
- You may need to use less z hop (z lift). I run 0.2mm. Too high gives me stringing.

There are a few factors that can affect your retraction settings, such as:
- Material type
- Print temperature
- Hotend
- Extruder
## Method

**We will be using using [:page_facing_up:SuperSlicer](https://github.com/supermerill/SuperSlicer/releases)'s calibration tools.**

- If you do not typically use SuperSlicer, you can start with one of the built-in Voron profiles for this test. 
    - The built-in profiles are not great in my opinion, but will work fine just for running the calibration tools. 
    - Shameless plug: try [:page_facing_up:my profiles](https://github.com/AndrewEllis93/Ellis-PIF-Profile) later on. There are some other warnings and dependencies, however *(please thoroughly read its readme)*, so just stick with the built-in ones for now.

We will be printing these retraction towers at three different temperatures. If you are confident that your filament temperature is well tuned, you may get good results with just one tower.

**1)** Ensure that your nozzle is clean. You can use a brass brush while it is heated.

**2)** Set your fan speed high.
- These are small towers, we don't want them to get melty.
- These are located in the "filament settings" tab, under "cooling".
- Try 80-100%.

**3)** Set your retract and unretract speeds to **30mm/s** to start. 
- This is located in the "printer settings" tab, under "extruder 1".
- I have had more luck with slower retraction speeds. Your mileage may vary.

**4)** Select "extruder retraction calibration" from the menu.

- ![](/images/Retraction-Menu.png) 

**5)** Click "remove fil. slowdown".

- ![](/images/Retraction-FilSlowdown.png) 

**6)** Fill out the parameters and select "Generate".

- ![](/images/Retraction-Params.png) 

    - **Start temp:**
        - Set a **bit higher** than your normal printing temps (maybe around 10C higher).
            - For this example, I will be using 255C with KVP ABS.
    - **Step:**
        - Direct drive: **0.1mm**
        - Bowden: **0.5mm**
    - **Height:**
        - Your maximum retraction length will be **(height - 1) * step**.
            - Do not exceed **1mm** for direct drive.\
            *(height: 11 when using a step of 0.1mm)*
                - You will *rarely* need more than this, but it is possible with some high flow hotends and setups. Start with 1mm, only go up to an absolute max of 2mm if required.
            - For bowden, this can vary. Try starting with a maximum of **3mm**. \
            *(height: 7 when using a step of 0.5mm)*
                - You may need more, depending on a few factors like pressure advance, bowden tube length, bowden tube internal diameter, and how firmly attached the tube is in the couplings.
                - Ensure that your bowden tubes are as firmly attached as possible, and do not [move too much in and out of their couplings during printing](https://youtu.be/lboDSH0945g?t=120). 
    - **Temp decrease (temp decr):**
        - **3x10°**.
            - This will print three retraction towers. One will be at your "start temp", the other two will be 10C increments below this.

    - You should get output like this:
        - ![](/images/Retraction-Sliced.png) 

**7) :warning: Arrange the towers front to back**\* **on your build plate.**
- These objects are printed one at a time. **This ensures that they are not knocked over by the gantry/toolhead.** 
- Arrange them from the hottest tower at the front, to coolest tower at the back.
    - The towers are printed from hottest to coldest. This just lowers the chance of collisions (particularly with poorly written `PRINT_END` macros). 
- ![](/images/Retraction-Sliced-FrontToBack.png)

    <sup>\* If you are using a different kinematic system than CoreXY/i3 cartesian, you may need to use a different arrangement. For example, a cross gantry would need diagonal.</sup>

**8) Print it, and inspect the results.** 
- If your hotter towers are much stringier, consider choosing a lower extrusion temperature.
- **To get your new retraction length:**
    - Count the rings (from the bottom), subtract 1, and multiply by your "step" value.
        - In my opinion, choose a height **1-2 rings higher** than where the stringing disappears. This just gives you a bit more headroom for filaments that may behave a bit differently.
        - We are subtracting 1 because the first ring is 0 retraction.