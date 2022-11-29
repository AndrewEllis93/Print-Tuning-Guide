[:arrow_left: Back to Table of Contents](/README.md)
# Bulging
## Bulging Layers

This may or may not just be a Prusa Slicer / SuperSlicer thing. I have not tested it in other slicers. 

- ![](/images/troubleshooting/bulging/Bulging2.png) 
    - Disable any "extra perimeters" and "supporting dense layer" settings (PS/SS)
    - Reduce perimeter accelerations.

## Bulges at STL Vertices
![](/images/troubleshooting/bulging/Vertex-Bulges.png)

![](/images/troubleshooting/bulging/Vertex-Bulges-2.png) 
- Your square corner velocity may be too low. (Did you leave it set at 1 by chance?)
- This can also be a sign that your perimeter speeds/accels are too high.

## Bulging Around Features (SuperSlicer)
- ![](/images/troubleshooting/bulging/feature_bulging.png) ![](/images/troubleshooting/bulging/feature-bulging-2.png) 

These types of bulges are often caused by **overextrusion of the supporting solid infill**:

- ![](/images/troubleshooting/bulging/feature_bulging-fill.png) 

First of all, you should tune your [:page_facing_up:pressure advance](/articles/pressure_advance.md) and [:page_facing_up:extrusion multiplier](/articles/extrusion_multiplier.md) using this guide's methods.

After that, see [:page_facing_up:Small Infill Areas Look Overextruded](/articles/troubleshooting/small_infill_areas_overextruded.md).\
When you have overextrusion issues in small areas, it greatly contributes to this issue.
- The above link goes into this in much more detail about this issue, but one of the larger improvements for me was to use these settings in SuperSlicer:
    - Top infill: "Not connected"
    - Solid infill: "Not connected"
    - Infill/perimeter overlap (encroachment): 20-25%
        - *(Lower is better, but don't go too low or your infill can disconnect from the perimeters)*

- There is some additional (advanced!) reading in that page with some more recent findings about a retraction trick. 
    - BUT that trick has downsides without using an **experimental** SuperSlicer build. **No support provided!**
## Bulging Patterns on Overhangs (SS)
![](/images/troubleshooting/bulging/AboveBridgeFlow-1.png)
![](/images/troubleshooting/bulging/AboveBridgeFlow-2.png)
![](/images/troubleshooting/bulging/AboveBridgeFlow-3.png)

- Some SuperSlicer profiles have "above the bridges" flow set to greater than 100%. This can cause the issues you see above. 
- There are three solutions:
    - **Set "threshold for bridge speed and fan" to 0**
        - This totally prevents SS from applying bridging settings to overhangs.
        - ![](/images/troubleshooting/bulging/AboveBridgeFlow-DisableOverhang.png)
    - **Set "threshold for bridge flow" to 0**
        - This prevents SS from applying *bridging flow* settings to overhangs, but still applies bridging speeds/fan settings.
        - ![](/images/troubleshooting/bulging/AboveBridgeFlow-DisableOverhangFlow.png)
    - **Reduce "above the bridges" flow to back to 100%**
        - ![](/images/troubleshooting/bulging/AboveBridgeFlow-Reset.png)
- If these do not fix it, it might instead be an [:page_facing_up:overheating issue.](/articles/cooling_and_layer_times.md)