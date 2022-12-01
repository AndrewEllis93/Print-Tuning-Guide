---
layout: default
title: Conditional Homing
#nav_order: 1
parent: Useful Macros
---
{% comment %} 
# This guide has moved! Please visit [the new site](https://ellis3dp.com/Print-Tuning-Guide/).
{% endcomment %}
# Conditional Homing
---
:dizzy: Macros are compatible with **Klipper only**.

---

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