---
layout: default
title: Conditional Homing
#nav_order: 1
parent: Useful Macros
---
# Conditional Homing

**Home if not already homed.** 

This is useful to throw at the beginning of other macros.
{% raw %}
```
[gcode_macro _CG28]
gcode:
    {% if "xyz" not in printer.toolhead.homed_axes %}
        G28
    {% endif %}
```
{% endraw %}