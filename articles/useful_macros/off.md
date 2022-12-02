---
layout: default
title: "Off"
#nav_order: 8
parent: Useful Macros
---
{% comment %} 
# This guide has moved! Please visit [the new site](https://ellis3dp.com/Print-Tuning-Guide/).
{% endcomment %}
# Off

---

{: .compat}
:dizzy: Macros are compatible with **Klipper only**.

---

Just an idea more than a copy-pastable macro as **yours will be different**. 

It's just handy to have a shortcut to turn off everything at once!

{% raw %}
```
[gcode_macro OFF]
gcode:
    M84                                  ; turn steppers off
    TURN_OFF_HEATERS                     ; turn bed / hotend off
    M107                                 ; turn print cooling fan off
    #SET_FAN_SPEED FAN=Exhaust SPEED=0   ; turn exhaust fan off
    #SET_FAN_SPEED FAN=BedFans SPEED=0   ; bed fan off
    #SET_PIN PIN=caselight VALUE=0       ; turn case light off
```
{% endraw %}