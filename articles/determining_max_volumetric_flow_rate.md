[:arrow_left: Back to Table of Contents](/README.md)
# Determining Maximum Volumetric Flow Rate

Volumetric flow rate indicates how much plastic that your hotend/extruder can extrude per second.

Volumetric flow is expressed in mm<sup>3</sup>/s (cubic millimeters per second).
## Why?
You can use this volumetric flow rate **to determine how fast your hotend/extruder is able to print.**

- See the [:pushpin:"how flow rate relates to speed"](/articles/determining_max_volumetric_flow_rate.md#how-volumetric-flow-rate-relates-to-print-speed) section to determine what maximum speeds you can print at with a given flow rate.

    - See the [:pushpin:"approximate values"](/articles/determining_max_volumetric_flow_rate.md#approximate-values) section for approximate values for certain hotends.

- Some slicers (including Prusa Slicer/SuperSlicer) let you configure this limit to ensure that you never outrun your hotend.

    - This means that you can change layer heights, nozzle sizes, line widths, and speeds without worrying about outrunning your hotend. 

    - You can also set any print speeds to a high "absolute maximum" speed (like infill) and let it be limited by the volumetric flow limit. This essentially prints at the maximum speed your hotend will allow:
        - This is utilized by my published SuperSlicer profile (see its [:page_facing_up:"Volumetric Speed Limiting"](https://github.com/AndrewEllis93/Ellis-PIF-Profile#volumetric-speed-limiting) section for more information.)

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

You should (generally) be okay using an approximate value and just lowering it if you have any issues. 

These are approximate values **assuming a standard brass 0.4mm nozzle.** 

Nozzle properties may affect these numbers. For example:
- Larger diameter nozzles will have higher flow rates
- Hardened steel has a lower thermal conductivity and you may get lower flow rates unless you compensate with higher temperatures. 
- Plated copper and tungsten carbide have higher thermal conductivity and might allow a bit higher flow rate. 
- Bondtech CHT nozzles use a different internal geometry that allows higher flow rates.

*If you want to get more scientific, test with a specific nozzle or setup, or your hotend just isn't listed, see [:pushpin:here](/articles/determining_max_volumetric_flow_rate.md#method) for a testing method.*

## How Volumetric Flow Rate Relates to Print Speed

Working out how quickly you can print at a given volumetric flow rate is quite simple:

- **speed = volumetric flow / layer height / line width**

Or, inversely,
- **volumetric flow = speed * line width * layer height**

For example, if your hotend is capable of 24mm<sup>3</sup>/sec, and you are printing with 0.4mm line width, at 0.2mm layer height:

- **24 / 0.4 / 0.2 = Maximum print speed of 300mm/sec**

## Formulas

**mm<sup>3</sup> = mm / 0.416**

Or, inversely, 

**mm = mm<sup>3</sup> * 0.416**

For example, if you extrude at **5mm/sec**, that comes out to **~12mm<sup>3</sup>/sec.** (5mm / 0.416)

\* <sup>*For 2.85mm filament, use 0.157 instead of 0.416.*</sup>\
\* <sup>*These fomulas are simplified versions of the cylinder volume equation (V=πr<sup>2</sup>h) given r and h or V, rounded to 3 significant figures. This is more than enough accuracy for our purposes (down to the thousandths). [:page_facing_up:Calculator](https://www.calculatorsoup.com/calculators/geometry-solids/cylinder.php)*</sup>

## Method

You will follow a similar process to extruder calibration. 

**1)** Heat your hotend. 

**2)** Extrude a little bit to ensure your E motor is energized and holding.

**3)** Mark a 120mm length of filament going into your extruder.

**4)** Extrude at increasing speeds. 
- At each interval, measure to ensure that exactly 100mm* entered the extruder.

- For example, the gcode to extrude at 5mm/sec is:
```
M83 ; Relative extrusion mode
G1 E100 F300 ; Extrude 100mm at 5mm/sec*
```
\* *Remember the the F speed is in mm/min, **not** mm/sec, so multiply your desired speed by 60.*

**5)** Keep increasing speeds and extruding until it starts dropping below 100mm\*. This is your max flow rate. 

- \* See the [:pushpin:"theory vs reality"](/articles/determining_max_volumetric_flow_rate.md#theory-vs-reality) section.

**6)** Convert the maximum extrusion speed you found to volumetric speed using the [:pushpin:formulas](/articles/determining_max_volumetric_flow_rate.md#formulas).

**7)** Set your new value in your slicer (in SuperSlicer, ctrl+f, search for "max_volumetric_speed").

- You should set your limit slightly lower in the slicer for margin of safety.

- Keep in mind that maximum volumetric flow rate can change with a number of factors, like temperatures, material, and nozzle type. 

- This value will work with most filaments. Sometimes, however, you may find a particular filament that doesn't flow as nicely. For these, (in PS/SS at least) you can set a volumetric flow override in that filament's "Filament Overrides" section.
## Theory vs Reality
Stephan from CNC Kitchen did some flow rate testing. He has a great article and video [:page_facing_up:here](https://www.cnckitchen.com/blog/flow-rate-benchmarking-of-a-hotend).

I don't want to steal his work, so here's an artist's rendition:

![](/images/extrusion-dropoff.png) 

*(you should really just visit the link)*


The main takeaway from this is that there is that **the closer you get to the absolute limit of your hotend (extruder skipping) , the more and more you will underextrude**.

Many people will actually set a higher volumetric flow rate limit, a bit past the point where this dropoff starts.

- For example, it doesn't really matter if you underextrude a few percent in infill. You can push infill speeds and just let them be capped by your volumetric flow limit (assuming your infill line widths are thick enough to compensate).

- It's up to you where your comfort zone is. Using the test above: 
    - **Stopping at 100mm:** guarantees that you will never underextrude due to speeds. 

    - **Stopping before skipping starts:** you can use this number and push speeds for things like infill, BUT you will need to be more vigilant about what speeds you are printing other features (such as perimeters) to prevent underextrusion and line gaps.

    - The numbers in the [:pushpin:"approximate values"](/articles/determining_max_volumetric_flow_rate.md#approximate-values) section are **somewhere in the middle** of the two extremes.