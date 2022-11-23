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
- ![](/images/troubleshooting/bulging/feature_bulging.png) 
    - Try this combination of settings. It will not make it *perfect*, but it made a noticeable improvement for me.\
    *(described in further detail in [:page_facing_up:Small Infill Areas Look Overextruded](/articles/troubleshooting/small_infill_areas_overextruded.md), but can have a positive effect for this issue too)*
        - Top infill: "Not connected"
        - Solid infill: "Not connected"
        - Infill/perimeter overlap (encroachment): 25%
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