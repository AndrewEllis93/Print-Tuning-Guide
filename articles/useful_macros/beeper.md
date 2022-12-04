---
layout: default
title: Beeper
#nav_order: 5
parent: Useful Macros
---
{% comment %} 
# This page has moved! Please visit [the new location](https://ellis3dp.com/Print-Tuning-Guide/articles/useful_macros/beeper.html).
{% endcomment %}
# Beeper
{: .no_toc }

---

{: .compat}
:dizzy: Macros are compatible with **Klipper only**.

---

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---
Allows you to utilize your LCD beeper. 
This requires you to specify your beeper pin as an output pin.
## PWM Beeper
A PWM beeper is more common nowadays, and is used on the common MINI12864 display.

Your `pin` may be different.
{% raw %}
```
[output_pin beeper]
pin: EXP1_1
value: 0
shutdown_value: 0
pwm: True
cycle_time: 0.0005 ; Default beeper tone in kHz. 1 / 0.0005 = 2000Hz (2kHz)
```
{% endraw %}

Usage:
- `BEEP`: Beep once with defaults.
- `BEEP I=3`: Beep 3 times with defaults.
- `BEEP I=3 DUR=200 FREQ=2000`: Beep 3 times, for 200ms each, at 2kHz frequency.

{% raw %}
```
[gcode_macro BEEP]
gcode:
    # Parameters
    {% set i = params.I|default(1)|int %}           ; Iterations (number of times to beep).
    {% set dur = params.DUR|default(100)|int %}     ; Duration/wait of each beep in ms. Default 100ms.
    {% set freq = params.FREQ|default(2000)|int %}  ; Frequency in Hz. Default 2kHz.

    {% for iteration in range(i|int) %}
        SET_PIN PIN=beeper VALUE=0.8 CYCLE_TIME={ 1.0/freq if freq > 0 else 1 }
        G4 P{dur}
        SET_PIN PIN=beeper VALUE=0
        G4 P{dur}
    {% endfor %}
```
{% endraw %}

This is the simple looping implementation. If you're feeling fancy, you can also [:page_facing_up: play tunes with it](https://github.com/majarspeed/Profiles-Gcode-Macros/tree/main/Beeper%20tunes). (Tune macros by Dustinspeed#6423)

## Non-PWM Beeper
Non-PWM beepers are used on some other displays such as the Ender 3 stock display.

Your `pin` will likely be different.
{% raw %}
```
[output_pin beeper]
pin: P1.30
value: 0
shutdown_value: 0
```
{% endraw %}
Usage: 
- `BEEP`: Beep once with defaults.
- `BEEP I=3`: Beep 3 times with defaults.
- `BEEP I=3 DUR=100`: Beep 3 times, for 100ms each.

{% raw %}
```
[gcode_macro BEEP]
gcode:
    # Parameters
    {% set i = params.I|default(1)|int %}        ; Iterations (number of times to beep).
    {% set dur = params.DUR|default(100)|int %}  ; Duration/wait of each beep in ms. Default 100ms.

    {% for iteration in range(i|int) %}
        SET_PIN PIN=beeper VALUE=1
        G4 P{dur}
        SET_PIN PIN=beeper VALUE=0
		G4 P{dur}
    {% endfor %}
```
{% endraw %}