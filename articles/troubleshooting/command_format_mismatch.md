# Error: "Command Format Mismatch"

Klipper consists of two parts. The "master" host software, and the "slave" MCU firmware. 

This error means that you updated Klipper software, but did not update the firmware on your MCUs.
- MCU stands for "microcontroller units". This refers to your printer control board(s) (SKR, Spider, Octopus, etc.)

**To fix this, re-compile and re-flash the firmware onto each MCU.**
- Refer to the example image below. Compare the version numbers in your error message to find out which MCUs need flashing.

    - The "host" version refers to the Klipper software. Each following version number refers to a specific MCU.

    - In this example, the "z" MCU is out of date:

    - ![](/images/troubleshooting/CommandFormatMismatch.png)

Refer to the [:page_facing_up:flashing documentation](https://docs.vorondesign.com/build/software/#firmware-flashing) for each specific board*.

- Check if your board supports [:page_facing_up:SD card updating](https://www.klipper3d.org/SDCard_Updates.html). It can save you from having to juggle SD cards.

    - Not all boards are supported this way. You may have to manually place firmware.bin on the SD card. 

    - I believe this is currently not working for Spider. Manually place firmware.bin on the SD card. 
- **This includes the [:page_facing_up:Pi MCU](https://www.klipper3d.org/RPi_microcontroller.html#building-the-micro-controller-code)** if configured (commonly used for accelerometer support).

Generally you should not update Klipper unless there is a specific feature or bug fix that you need.

\* *Some MCUs are not yet documented on the Voron documentation site. Find the directions from the vendor. Most of them have a github repository with manuals.*