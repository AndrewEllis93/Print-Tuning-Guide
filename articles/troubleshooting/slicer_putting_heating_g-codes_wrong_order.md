---
layout: default
title: Slicer is Putting Heating G-codes in the Wrong Place/Order
#nav_order: 11
parent: Troubleshooting
---
# Slicer is Putting Heating G-codes in the Wrong Place/Order

For example:

- Your `PRINT_START` macro is running before your hotend or bed heat up. 

- Or you wish for your heating commands to come after `PRINT_START`, or to have one heater to heat before your start g-code, and one after.

The two options below allow you to control this order.

- Pass variables to `PRINT_START` (allows the most control, but is more complex)
    - See the *"Passing Variables to PRINT_START"* article 
    [:page_facing_up: here](http://localhost:4000/Print-Tuning-Guide/articles/passing_slicer_variables.html).

- Force g-code ordering (only allows changing the g-code order, but is easy to set up)

    - See the *"Controlling Slicer Temperature G-Code Order (Simple Method)"* article [:page_facing_up: here](http://localhost:4000/Print-Tuning-Guide/articles/controlling_slicer_g-code_order.html).

