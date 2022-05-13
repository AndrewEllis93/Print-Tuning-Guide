[:arrow_left: Back to Table of Contents](/README.md)
# Passing Slicer Variables to PRINT_START

This section will demonstrate passing temperature variables to PRINT_START.

**This method can be used for other slicer variables too, not just temperatures / heating commands.**
- The available variables are not always published, however, so you sometimes need to dig around to find the names of them.
- SuperSlicer recently introduced [:page_facing_up:support for custom variables](https://github.com/supermerill/SuperSlicer/releases/tag/2.3.57.5).


## Passing Temperatures

By default, slicers will put heating commands either entirely before or after `PRINT_START`. You have to pass the temps TO `PRINT_START` in order to control when they happen. 
For example I don’t want my nozzle to heat until the very end so it’s not oozing during QGL, mesh etc.

If you don’t use a chamber thermistor, just remove the chamber stuff. 

### Example macro:

This macro is a **template**. \
You will have to add things like `G32`,`QUAD_GANTRY_LEVEL`,`BED_MESH_CALIBRATE`, or whatever other routines that you need to run during your `PRINT_START`.

```
[gcode_macro PRINT_START]
gcode:        
    # Parameters
    {% set bedtemp = params.BED|int %}
    {% set hotendtemp = params.HOTEND|int %}
    {% set chambertemp = params.CHAMBER|default(0)|int %}
    
    G28
    # <insert your routines here>
    M190 S{bedtemp}                                                              ; set & wait for bed temp
    TEMPERATURE_WAIT SENSOR="temperature_sensor chamber" MINIMUM={chambertemp}   ; wait for chamber temp
    # <insert your routines here>
    M109 S{hotendtemp}                                                           ; set & wait for hotend temp
    # <insert your routines here>
    G28 Z                                                                        ; final z homing
```

This would now be run like `PRINT_START BED=110 HOTEND=240 CHAMBER=50`. 
Chamber defaults to 0 if not specified.
### Slicer Start G-code

Don't split any of these lines.
#### SuperSlicer
(3 lines)
 ```    
M104 S0 ; Stops PS/SS from sending temp waits separately
M140 S0
PRINT_START BED=[first_layer_bed_temperature] HOTEND={first_layer_temperature[initial_extruder]+extruder_temperature_offset[initial_extruder]} CHAMBER=[chamber_temperature]
```
![](/images/PassingVariables-SS.png) 

#### Prusa Slicer 
(3 lines)

*Prusa Slicer doesn’t support chamber temp.*
    
```
M104 S0 ; Stops PS/SS from sending temp waits separately
M140 S0
PRINT_START BED=[first_layer_bed_temperature] HOTEND=[first_layer_temperature[initial_extruder]]
```
![](/images/PassingVariables-PS.png) 

#### Cura
(1 line)
```
PRINT_START BED={material_bed_temperature_layer_0} HOTEND={material_print_temperature_layer_0} CHAMBER={build_volume_temperature}
```
![](/images/PassingVariables-Cura.png) 