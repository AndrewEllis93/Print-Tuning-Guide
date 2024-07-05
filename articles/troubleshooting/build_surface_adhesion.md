---
layout: default
title: Build Surface Adhesion
parent: Troubleshooting
---
{% comment %} 
# This page has moved! Please visit [the new location](https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting/build_surface_adhesion.html).
{% endcomment %}

# Build Surface Adhesion
{: .no_toc }

---

{: .compat}
:dizzy: This page is compatible with all printers.

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

{: .attention }
>- **:warning: Thoroughly wash all print surfaces with dish soap and water**.
>    - You should do this **even for brand new surfaces.**
>    - Use some elbow grease, especially with textured plates. Scrub thoroughly in small circles and then rinse.*
>    - :warning: Don't dry it using cloth. Many laundry products contain fats, oils, or waxes. You may use paper towels\*\*, or preferably, **air dry it**.
>- :warning: Avoid touching your build surface as much as possible. Oils from your fingers will cause adhesion issues. Pick it up using the tabs, or by the sides. You may also handle it with paper towels**
>- Isopropyl alcohol does not do a great job of cleaning oils. It's okay for maintenance, but you should still plan to wash it occasionally.

\* *If your build surface is not detachable, carefully spritz it with water or use isopropyl alcohol. Be thorough - you don't want any remaining soap residue.*\
\*\* *Some brands of paper towels contain conditioners that may cause issues.*

---

{: .note }

### Smooth PEI

- **Consider scuffing it up** with a [:page_facing_up: kitchen scouring pad](https://www.scotch-brite.com/3M/en_US/scotch-brite/tools/~/Scotch-Brite-Heavy-Duty-Scour-Pad/?N=4337+3294529207+3294631680&rt=rud).

    - **This helps immensely**, much like how you would scuff/sand a surface before painting or gluing something to it.

    - Some people choose not to do this, to keep the glass-like surface finish on their prints. However, *you will be sacrificing adhesion* and may need to use brims and/or adhesives on occasion.

    - ~800-1000 grit sandpaper or the scrubby side of a fresh sponge may also work.

    - You can refresh the surface this way on occasion, just remember to wash it again afterwards.

    - You should probably keep the scouring pad/sponge out of the kitchen afterwards. I'm not sure the health effects of plastic dust ending up on your dishes - better safe than sorry!

### All Surfaces

- Ensure that you are using a proper first layer temperature.\
Some filament brands recommend inaccurate/conservative temperatures. Try standard temps instead if you are having issues.
    - PLA: ~60C
    - PETG: ~80C
    - ABS: ~90-100C*
        - *:warning: Voron V2 and Trident have a ~10-15C temperature drop due to the thickness of the bed. Most people run ~110C for ABS because of this.


- :warning: Ensure that your [:page_facing_up: first layer squish](../first_layer_squish.md) is correct.

- Use adequately thick line widths (in your slicer) for your first layer.
    - I use [:page_facing_up: **120%**](../a_note_about_line_width.md) normally, but higher line widths can further increase adhesion. 
        - Thicker widths create more pressure against the build surface, resulting in a better bond.

- Ensure your PEI is not counterfeit. You may have to ask in the Discord for others' experiences with a given brand. If your PEI is clear rather than yellowish, it's fake.
    - Stick to well-known brands. 
    - This is common with unknown AliExpress and Amazon sellers.

- Ensure that your build surface is actually meant for printing. Some plates *appear* to be two-sided (yellow/orange coloring for aesthetics) but are actually only one-sided.

- Instead of PEI (or to supplement your PEI), you can use adhesives like [:page_facing_up: Vision Miner Nano Polymer](https://smile.amazon.com/dp/B09JQWFVY3/ref=twister_B09JRGDWFT), [:page_facing_up: Magigoo](https://www.amazon.com/Magigoo-Pen-All-One-Adhesive/dp/B01N2JGTWJ), or a [:page_facing_up: DIY alternative](https://discord.com/channels/460117602945990666/461133450636951552/975445247637217362).
    - (Not sponsored) Vision Miner Nano Polymer, while a bit expensive, is excellent.
    
        - There is a $19 50ml bottle on Amazon but it's not always in stock. 50ml goes a long way, especially if you dilute it.
        - Dilute it 1:1 to 3:1 isopropyl alcohol to adhesive - it will last longer and is much easier to spread.
        - It grips like crazy. 
            - (Though sometimes it grips *too* much. It can pull chunks out of glass or pull texture off of beds if too much is used. Less is more!)
        - It doesn't leave sticky residue (it does leave some slight whitish coloring though, which can be easily cleaned with IPA)
        - It often lasts a few prints between applications.
        - It (usually) releases when cooled, assuming you didn't use too much.

### Textured PEI

- Textured PEI often needs a little more squish than smooth PEI. This pushes the filament into the voids.

### Last Resort
As a **very last resort**, you can try refreshing the surface with acetone. 

Keep in mind, however, that:
 - :warning: This weakens PEI over time.
 - :warning: It can **destroy** certain surfaces (mainly certain brands of textured sheets). 
 
 **Only try this if it's going in the trash otherwise.**
