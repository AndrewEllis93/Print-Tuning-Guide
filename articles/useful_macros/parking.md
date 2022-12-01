---
layout: default
title: Parking
#nav_order: 7
parent: Useful Macros
---
# Parking
---
:dizzy: Macros are compatible with **Klipper only**.

---

Park the toolhead at different places. Automatically determined based on your printer's configured size.

{% raw %}
```
# Park front center
[gcode_macro PARKFRONT]
gcode:
    {% if "xyz" not in printer.toolhead.homed_axes %}
        G28                           ; home if not already homed
    {% endif %}
    SAVE_GCODE_STATE NAME=PARKFRONT
    G90                               ; absolute positioning
    G0 X{printer.toolhead.axis_maximum.x/2} Y{printer.toolhead.axis_minimum.y+5} Z{printer.toolhead.axis_maximum.z/2} F6000        
    RESTORE_GCODE_STATE NAME=PARKFRONT
```
{% endraw %}
{% raw %}
```
# Park front center, but low down.
[gcode_macro PARKFRONTLOW]
gcode:
    {% if "xyz" not in printer.toolhead.homed_axes %}
        G28                           ; home if not already homed
    {% endif %}
    SAVE_GCODE_STATE NAME=PARKFRONT
    G90                              ; absolute positioning
    G0 X{printer.toolhead.axis_maximum.x/2} Y{printer.toolhead.axis_minimum.y+5} Z20 F6000                                     
    RESTORE_GCODE_STATE NAME=PARKFRONT
```
{% endraw %}
{% raw %}
```
# Park top rear left
[gcode_macro PARKREAR]
gcode:
    {% if "xyz" not in printer.toolhead.homed_axes %}
        G28                           ; home if not already homed
    {% endif %}
    SAVE_GCODE_STATE NAME=PARKREAR
    G90                              ; absolute positioning
    G0 X{printer.toolhead.axis_minimum.x+10} Y{printer.toolhead.axis_maximum.y-10} Z{printer.toolhead.axis_maximum.z-50} F6000     
    RESTORE_GCODE_STATE NAME=PARKREAR
```
{% endraw %}
{% raw %}
```
# Park at center of build volume
[gcode_macro PARKCENTER]
gcode:
    {% if "xyz" not in printer.toolhead.homed_axes %}
        G28                           ; home if not already homed
    {% endif %}
    SAVE_GCODE_STATE NAME=PARKCENTER
    G90                               ; absolute positioning
    G0 X{printer.toolhead.axis_maximum.x/2} Y{printer.toolhead.axis_maximum.y/2} Z{printer.toolhead.axis_maximum.z/2} F6000    
    RESTORE_GCODE_STATE NAME=PARKCENTER
```
{% endraw %}
{% raw %}
```
# Park 15mm above center of bed
[gcode_macro PARKBED]
gcode:
    {% if "xyz" not in printer.toolhead.homed_axes %}
        G28                           ; home if not already homed
    {% endif %}
    SAVE_GCODE_STATE NAME=PARKBED
    G90                                ; absolute positioning
    G0 X{printer.toolhead.axis_maximum.x/2} Y{printer.toolhead.axis_maximum.y/2} Z15 F6000                                     
    RESTORE_GCODE_STATE NAME=PARKBED
```
{% endraw %}
