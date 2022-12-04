---
layout: default
title: Conditional Homing
#nav_order: 1
parent: Useful Macros
---
{% comment %} 
# This page has moved! Please visit [the new location](https://ellis3dp.com/Print-Tuning-Guide/articles/useful_macros/conditional_homing.html).
{% endcomment %}
# Conditional Homing

---

{: .compat}
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