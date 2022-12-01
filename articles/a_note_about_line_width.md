---
layout: default
title: A Note About Line Width
nav_order: 1
parent: Before We Begin
---
{% comment %} 
# This guide has moved! Please visit [the new site](http://ellis3dp.com/Print-Tuning-Guide/).
{% endcomment %}

# A Note About Line Width
Any line widths in this guide are expressed as a **percentage of nozzle diameter.** \
This allows the guide to remain agnostic to nozzles.

SuperSlicer natively allows percentages to be entered this way.

However: 
- Prusa Slicer bases percentages on layer heights instead.
- Cura does not allow percentages at all. 
- Other slicers may or may not support this.

**:warning: For Cura / Prusa Slicer / possibly others, you MUST use static line widths.** \
For example, enter **0.48mm** instead of **120%** if you are using a 0.4mm nozzle.

