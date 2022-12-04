---
layout: default
title: Infill/Perimeter Overlap
nav_order: 9
parent: Tuning
---
{% comment %} 
# This page has moved! Please visit [the new location](https://ellis3dp.com/Print-Tuning-Guide/articles/infill_perimeter_overlap.html).
{% endcomment %}
# Infill/Perimeter Overlap
---

{: .compat}
:dizzy: This page is compatible with all printers.

---

After tuning flow and pressure advance, you may still have some pinholes where your top infill meets your perimeters. This is more prevalent in PS/SS.

This is *not necessarily* an indicator that your flow or pressure advance are wrong, though they can impact it. 

One approach is to [:page_facing_up: set top infill to "not connected"](./troubleshooting/small_infill_areas_overextruded.md#not-connected-top-infill-superslicer) (SS). This has some other potential benefits, and often fixes the pinholes without having to do any overlap tweaking.

For "connected" infill, simply adjust "infill/perimeter overlap" (PS) or "infill/perimeters encroachment" (SS) until satisfied. I ended up at about 40%. 

*(Though now I use the default overlap of 25% with "not connected" top infill instead.)*

## Examples
- ![](./images/infill_perimeter_overlap/Overlap-1.png) 
- ![](./images/infill_perimeter_overlap/Overlap-2.png) 
## Overlap Tweaked:

- ![](./images/infill_perimeter_overlap/Overlap-Fixed1.png) 

