---
layout: default
title: Replace M109/M190 With TEMPERATURE_WAIT
#nav_order: 11
parent: Useful Macros
---
# Replace `M109`/`M190` With `TEMPERATURE_WAIT`
Replace `M109` (wait for hotend temperature) and `M190` (wait for bed temperature) with TEMPERATURE_WAIT.

This just makes Klipper resume immediately after reaching temp. Otherwise it waits for the temperature to stabilize.

## M109
{% raw %}
```
[gcode_macro M109]
rename_existing: M99109
gcode:
    #Parameters
    {% set s = params.S|float %}
    
    M104 {% for p in params %}{'%s%s' % (p, params[p])}{% endfor %}  ; Set hotend temp
    {% if s != 0 %}
        TEMPERATURE_WAIT SENSOR=extruder MINIMUM={s} MAXIMUM={s+1}   ; Wait for hotend temp (within 1 degree)
    {% endif %}
```
{% endraw %}

## M190
:warning: If you are using my [:page_facing_up: bed fan](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/Ellis/Bed_Fans) macros, **do not use this version.** Those macros include a variant of this with other essential functions.

{% raw %}
```
[gcode_macro M190]
rename_existing: M99190
gcode:
    #Parameters
    {% set s = params.S|float %}

    M140 {% for p in params %}{'%s%s' % (p, params[p])}{% endfor %}   ; Set bed temp
    {% if s != 0 %}
        TEMPERATURE_WAIT SENSOR=heater_bed MINIMUM={s} MAXIMUM={s+1}  ; Wait for bed temp (within 1 degree)
    {% endif %}
```
{% endraw %}