---
layout: default
title: Dump Variables
#nav_order: 9
parent: Useful Macros
---
# Dump Variables
This dumps all current Klipper variables to the g-code terminal. 

This helps to find Klipper system variables for use in macros. A filter for both name and value can be applied.

{% raw %}
```
[gcode_macro DUMP_VARIABLES]
gcode:
    {% set filter_name = params.NAME|default('')|string|lower %}
    {% set filter_value = params.VALUE|default('')|string|lower %}
    {% set show_cfg = params.SHOW_CFG|default(0)|int %}
    
    {% set out = [] %}

    {% for key1 in printer %}
        {% for key2 in printer[key1] %}
            {% if (show_cfg or not (key1|lower == 'configfile' and key2|lower in ['config', 'settings'])) and (filter_name in key1|lower or filter_name in key2|lower) and filter_value in printer[key1][key2]|string|lower %}
                {% set dummy = out.append("printer['%s'].%s = %s" % (key1, key2, printer[key1][key2])) %}
            {% endif %}
        {% else %}
            {% if filter_name in key1|lower and filter_value in printer[key1]|string|lower %}
                {% set dummy = out.append("printer['%s'] = %s" % (key1, printer[key1])) %}
            {% endif %}
        {% endfor %}
    {% endfor %}
    
    {action_respond_info(out|join("\n"))}

```
{% endraw %}

*The filtering functionality was contributed by [:page_facing_up: FatalBulletHit](https://github.com/FatalBulletHit). Thanks!*
## Arguments
- `NAME` *(string)* - Filter results based on name (only show varables with names containing this string)
- `VALUE` *(string)* - Filter results based on value (only show values containing this value)
- `SHOW_CFG` *(integer, 0-1)* - Set to 1 to include entire config in output. Default 0 (config filtered out)

## Examples
- `DUMP_VARIABLES`: Returns all variables (excluding `printer['configfile'].config` and `printer['configfile'].settings` as they contain the entire config).
- `DUMP_VARIABLES NAME=stepper`: Returns all variables which have the string `stepper` in their name.
- `DUMP_VARIABLES VALUE=extruder` : Returns all variables which have the string `extruder` in their value.
- `DUMP_VARIABLES NAME=stepper VALUE=extruder` : Returns all variables which have the string `stepper` in their name and the string `extruder` in their value.
- `DUMP_VARIABLES SHOW_CFG=1` : Returns all variables, including the config.