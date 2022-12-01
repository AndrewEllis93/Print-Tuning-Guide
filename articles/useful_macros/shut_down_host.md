---
layout: default
title: Shut Down Host
#nav_order: 8
parent: Useful Macros
---
{% comment %} 
# This guide has moved! Please visit [the new site](https://andrewellis93.github.io/Print-Tuning-Guide/).
{% endcomment %}
# Shut Down Host
---
:dizzy: Macros are compatible with **Klipper only**.

---

OctoPrint and Moonraker use different shutdown commands, but it doesn't hurt to have both.

I also throw in commands to turn off everything else first, otherwise your case lighting / neopixels etc will stay on.

{% raw %}
```
[gcode_macro SHUTDOWN]
gcode:
    #LCDRGB R=0 G=0 B=0                               ; Turn off LCD neopixels (see above for this macro)
    #OFF                                              ; Shortcut to turn everything off (see above for this macro)
    {action_respond_info('action:poweroff')}          ; OctoPrint compatible host shutdown
	{action_call_remote_method("shutdown_machine")}   ; Moonraker compatible host shutdown
```
{% endraw %}

Then you can add it to the "setup" menu of your LCD with this:
{% raw %}
```
[menu __main __setup __shutdown]
type: command
enable: {not printer.idle_timeout.state == "Printing"}
name: Shut down
gcode: SHUTDOWN
```
{% endraw %}

Or the "control" menu, if you prefer, with this:
{% raw %}
```
[menu __main __control __shutdown]
type: command
enable: {not printer.idle_timeout.state == "Printing"}
name: Shut down
gcode: SHUTDOWN
```
{% endraw %}