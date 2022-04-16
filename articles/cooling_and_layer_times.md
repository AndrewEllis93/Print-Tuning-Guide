[:arrow_left: Back to Table of Contents](/README.md)
# Cooling and Layer Times
## Signs of Overheating
![](/images/Overheating-1.png) ![](/images/Overheating-4.png) 
![](/images/Overheating-2.png) 
![](/images/Overheating-3.png) 
![](/images/Overheating-5.png) 
![](/images/Overheating-6.jpg) 
## How to Fix It

People often start printing by ABS with no cooling. While this is valid advice for unenclosed printers, it's not a universal rule. **ABS often needs some cooling, especially in an enclosure.**

There are multiple things you can do to minimize overheating with ABS.

**1) Increase fan speeds.**

- The higher your chamber temperature is, the more fan speed you will need.
- Use constant fan speeds when possible. For filaments that shrink, **varying fan speeds during a print will cause inconsistent layers and banding.** Some layers will essentially shrink more than others.
- You probably need higher fan speeds than you think. 
    - The hotter your enclosure, the higher fan speeds you will need.
        - For example I run AB-BN (5015 fan mod) and have a 63C chamber.
            - For large plates, I use 40% fan.
            - For small plates, I may use up to 80% fan.
            - For single small objects, I may use up to 100% fan.
    - For very large objects, you may want to be more conservative with cooling. Large objects are much more prone to warping.
        - This is the only time I might use differing fan speeds. Lower fan speeds for the majority of the print, with higher fan speeds for overhangs.
- If your prints are curling away from the bed even at low fan speeds, it may actually be a [:page_facing_up:build surface adhesion](/articles/build_surface_adhesion.md) issue.


**2) Increase "minimum layer time" / "layer time goal" / "slow down if layer print time is below"**
- Under filament cooling settings in PS/SS. 
    - You can use **ctrl+f** to find settings by name.
- I set this to a minimum of 15 seconds.
- This essentially slows down the print for very short/small layers, allowing each layer adequate time to cool.
- When layer times are **too short**, they do not have enough time to properly cool. You will then be printing on top of layers that are still soft.

**3) Print more objects at once, and spread them out.**

- We can allow objects to have some "break time" between layers simply by printing more objects at once. Spread them out to induce more travel time, and maybe even reduce travel speeds.
- ![](/images/Cooling-Spread.png) 