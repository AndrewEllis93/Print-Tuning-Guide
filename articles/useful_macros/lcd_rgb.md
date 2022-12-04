---
layout: default
title: LCD RGB
#nav_order: 6
parent: Useful Macros
---
{% comment %} 
# This page has moved! Please visit [the new location](https://ellis3dp.com/Print-Tuning-Guide/articles/useful_macros/lcd_rgb.html).
{% endcomment %}
# LCD RGB

---

{: .compat}
:dizzy: Macros are compatible with **Klipper only**.

---

This just provides an easy shortcut to change your neopixel LCD color. This may need modifying depending on your particular LCD. Mine is an MINI12864.

I have my LCD turn red during runouts, and green during filament swaps.

Example usage: `LCDRGB R=0.8 G=0 B=0`

Colors will default to off if not specified. For example, `LCDRGB G=1` can act as shorthand to change the color to green (turning off red/blue).

{% raw %}
```
[gcode_macro LCDRGB]
gcode:
    {% set r = params.R|default(0)|float %}
    {% set g = params.G|default(0)|float %}
    {% set b = params.B|default(0)|float %}

    SET_LED LED=lcd RED={r} GREEN={g} BLUE={b} INDEX=1 TRANSMIT=0
    SET_LED LED=lcd RED={r} GREEN={g} BLUE={b} INDEX=2 TRANSMIT=0
    SET_LED LED=lcd RED={r} GREEN={g} BLUE={b} INDEX=3
```
{% endraw %}

To reset the RGB / set the initial RGB. (**set your default LCD colors here**, and use `INITIAL_RGB` to call set it back.)
{% raw %}
```
[gcode_macro INITIAL_RGB]
gcode:
    SET_LED LED=lcd RED=1 GREEN=0.45 BLUE=0.4 INDEX=1 TRANSMIT=0
    SET_LED LED=lcd RED=0.25 GREEN=0.2 BLUE=0.15 INDEX=2 TRANSMIT=0
    SET_LED LED=lcd RED=0.25 GREEN=0.2 BLUE=0.15 INDEX=3
```
{% endraw %}

To set the default colors at startup (required)
{% raw %}
```
[delayed_gcode SETDISPLAYNEOPIXEL]
initial_duration: 1
gcode:
    INITIAL_RGB
```
{% endraw %}