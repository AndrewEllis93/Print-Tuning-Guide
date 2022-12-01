---
layout: default
title: Conditional QGL
#nav_order: 2
parent: Useful Macros
---
# Conditional QGL
---
:dizzy: Macros are compatible with **Klipper only**.

---
QGL if not already done.

I don't personally use this, I prefer to QGL every print. But some people like it.
{% raw %}
```
[gcode_macro _CQGL]
gcode:
    {% if printer.quad_gantry_level.applied == False %}
        {% if "xyz" not in printer.toolhead.homed_axes %}
            G28 ; home if not already homed
        {% endif %}
        QUAD_GANTRY_LEVEL
        G28 Z
    {% endif %}
```
{% endraw %}