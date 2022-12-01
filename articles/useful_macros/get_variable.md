---
layout: default
title: Get Variable
#nav_order: 10
parent: Useful Macros
---
# Get Variable
---
:dizzy: Macros are compatible with **Klipper only**.

---
*Contributed by [:page_facing_up: FatalBulletHit](https://github.com/FatalBulletHit). Thanks!*

This returns value and type of a single variable to the g-code terminal. Keys and indexes can be chained to access nested dictionaries and lists.
{% raw %}
```
[gcode_macro GET_VARIABLE]
gcode:
    {% set names = (params.NAME).split('.')|list %}
    {% set join = (params.JOIN)|default(1)|int %}
    
    {% set _dummy0 = namespace( break = 0 ) %}
    {% set _dummy1 = namespace( out = printer[names|first] ) %}
    
    {% for name in names if _dummy0.break == 0 %}
        {% if loop.index > 1 %}
            {% if name in _dummy1.out %}
                {% set _dummy1.out = _dummy1.out[name] %}
            {% elif name[0] in '0123456789' and _dummy1.out is iterable and _dummy1.out is not string and _dummy1.out is not mapping and _dummy1.out|length > name[0]|int %}
                {% set _dummy1.out = _dummy1.out[name|int] %}
            {% else %}
                {% set _dummy0.break = loop.index0 %}
            {% endif %}
        {% endif %}
    {% endfor %}
    
    {% if _dummy1.out is boolean %}
        { action_respond_info('Type: boolean') }
    {% elif _dummy1.out is float %}
        { action_respond_info('Type: float') }
    {% elif _dummy1.out is integer %}
        { action_respond_info('Type: integer') }
    {% elif _dummy1.out is mapping %}
        { action_respond_info('Type: mapping') }
    {% elif _dummy1.out is string %}
        { action_respond_info('Type: string') }
    {% elif _dummy1.out is iterable %}
        { action_respond_info('Type: iterable') }
    {% elif _dummy1.out is none %}
        { action_respond_info('Type: none') }
    {% elif _dummy1.out is undefined %}
        { action_respond_info('Type: undefined') }
    {% elif _dummy1.out is callable %}
        { action_respond_info('Type: callable') }
    {% else %}
        { action_respond_info('Type: unknown') }
    {% endif %}
    
    {% if join and _dummy1.out is iterable and _dummy1.out is not string and _dummy1.out is not mapping %}
        { action_respond_info('%s' % _dummy1.out|join("\n")) }
    {% else %}
        { action_respond_info('%s' % _dummy1.out) }
    {% endif %}
    
    {% if _dummy0.break != 0 %}
        { action_respond_info('"printer.%s" does not contain "%s"!' % (names[0:_dummy0.break]|join('.'), names[_dummy0.break])) }
    {% endif %}
```
{% endraw %}
## Arguments
- `NAME` *(string) (required)* - Specify the name of the variable that you want to retreive.

## Examples
- `GET_VARIABLE NAME=toolhead`: Returns value and type of variable `printer.toolhead`.
- `GET_VARIABLE NAME=bed_mesh.profiles.default.points.1.0`: Returns value and type of variable `printer.bed_mesh.profiles.default.points[1][0]`.

