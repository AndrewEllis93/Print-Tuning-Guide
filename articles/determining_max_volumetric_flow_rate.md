# Determining Maximum Volumetric Flow Rate

Volumetric flow rate indicates how much plastic that your hotend/extruder can extrude per second.

Volumetric flow is expressed in mm<sup>3</sup>/sec (cubic millimeters per second).
## Why?
You can use this volumetric flow rate **to determine how fast your hotend/extruder is able to print.**

- See [:pushpin:this section](/articles/determining_max_volumetric_flow_rate.md#how-volumetric-flow-rate-relates-to-print-speed) to determine what maximum speeds you can print at with a given flow rate.
    - See [:pushpin:the next section](/articles/determining_max_volumetric_flow_rate.md#approximate-values) for approximate values for certain hotends.
- Some slicers (including Prusa Slicer/SuperSlicer) let you configure this limit to ensure that you never outrun your hotend.
    - This means that you can change layer heights, nozzle sizes, line widths, and speeds without worrying about outrunning your hotend. 
    - You can also set any print speeds to a high "absolute maximum" speed (like infill) and let it be limited by the volumetric flow limit. This essentially prints at the maximum speed your hotend will allow:
        - This is utilized by my published SuperSlicer profile (see the [:page_facing_up:"Volumetric Speed / Auto Speed" section](https://github.com/AndrewEllis93/Ellis-PIF-Profile#volumetric-speed--auto-speed) for more information.)
        - ![](/images/Volumetric-SS.png) 
## Approximate Values

| Hotend     | Flow Rate (mm<sup>3</sup>/sec) |
| :---        |    :----:   |
| E3D V6            | 11
| E3D Revo            | 15
| Dragon SF| 15
| Dragon HF| 24
| Mosquito| 20
| Mosquito Magnum| 30

You should be okay using an approximate value and just lowering it if you have any issues. 

These are approximate values **assuming a standard brass 0.4mm nozzle.** 

Nozzle properties may affect these numbers. For example:
- Larger diameter nozzles will have higher flow rates
- Hardened steel has a lower thermal conductivity and you may get lower flow rates unless you compensate with higher temperatures. 
- Plated copper and tungsten carbide have higher thermal conductivity and might allow a bit higher flow rate. 
- Bondtech CHT nozzles use a different internal geometry that allows higher flow rates.

*If you want to get more scientific, test with a specific nozzle or setup, or your hotend just isn't listed, see [here](/articles/determining_max_volumetric_flow_rate.md#method for a testing method.*

## How Volumetric Flow Rate Relates to Print Speed

Working out how quickly you can print at a given volumetric flow rate is quite simple:

- **speed = volumetric flow / layer height / line width**

Or, inversely,
- **volumetric flow = speed * line width * layer height**

For example, if your hotend is capable of 24mm<sup>3</sup>/sec, and you are printing with 0.4mm line width, at 0.2mm layer height:

- **24 / 0.4 / 0.2 = Maximum print speed of 300mm/sec**

## Method
You will follow a similar process to extruder calibration. 

This is a rough calculation. Maximum volumetric flow rate can change with a number of factors, like temperatures, material, and nozzle type. 

You should set your limit slightly lower in the slicer for margin of safety, and to avoid having to re-tune for different filaments that don't flow as nicely.

**1)** Heat your hotend. \
**2)** Extrude a little bit to ensure your E motor is energized and holding.\
**3)** Mark a 120mm length of filament going into your extruder.\
**4)** Extrude at increasing speeds. At each interval, measure to ensure that exactly 100mm entered the extruder.

For example, the gcode to extrude at 5mm/sec is:
```
M83 ; Relative extrusion mode
G1 E100 F300 ; Extrude 100mm at 5mm/sec
```
Remember the the F speed is in mm/min, **not** mm/sec, so multiply your desired speed by 60.

**5)** Keep increasing speeds and extruding until it starts dropping below 100mm. This is your max flow rate. \
**6)** Convert your extrusion speed to volumetric speed using the below formulas. \
**7)** Enter a slightly lower volumetric speed into the slicer.

## Formulas

**mm<sup>3</sup> = mm / 0.416**

Or, inversely, 

**mm = mm<sup>3</sup> * 0.416**

For example, if you extrude at **5mm/sec**, that comes out to **~12mm<sup>3</sup>/sec.** (5mm / 0.416)

\* <sup>*For 2.85mm filament, use 0.157 instead of 0.416.*</sup>\
\* <sup>*These fomulas are simplified versions of the cylinder volume equation (V=πr<sup>2</sup>h) given r and h or V, rounded to 3 significant figures. This is more than enough accuracy for our purposes (down to the thousandths). [:page_facing_up:Calculator](https://www.calculatorsoup.com/calculators/geometry-solids/cylinder.php)*</sup>
