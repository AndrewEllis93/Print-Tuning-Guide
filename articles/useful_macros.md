[:arrow_left: Back to Table of Contents](/README.md)

# Useful Macros

# Conditional Homing

Home if not already homed. Useful to throw at the beginning of other macros. This is used in many of the other macros below.
```
[gcode_macro CG28]
gcode:
    {% if "xyz" not in printer.toolhead.homed_axes %}
        G28
    {% endif %}
```
# Beeper
Allows you to utilize your LCD beeper. 
This requires you to specify your beeper pin as an output pin.
## PWM Beeper
A PWM beeper is more common nowadays, and is used on the common MINI12864 display.

Your `pin` may be different.
```
[output_pin beeper]
pin: EXP1_1
value: 0
shutdown_value: 0
pwm: True
cycle_time: 0.0005 ; Default beeper tone in kHz. 1 / 0.0005 = 2000Hz (2kHz)
```

Usage:
- `BEEP`: Beep once with defaults.
- `BEEP I=3`: Beep 3 times with defaults.
- `BEEP I=3 DUR=200 FREQ=2000`: Beep 3 times, for 200ms each, at 2kHz frequency.

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

This is the simple looping implementation. If you're feeling fancy, you can also [play tunes with it](https://github.com/majarspeed/Profiles-Gcode-Macros/tree/main/Beeper%20tunes). (Tune macros by Dustinspeed#6423)

## Non-PWM Beeper
Non PWM beepers are used on some other displays such as the Ender 3 stock display.

Your `pin` will likely be different.
```
[output_pin beeper]
pin: P1.30
value: 0
shutdown_value: 0
```
Usage: 
- `BEEP`: Beep once with defaults.
- `BEEP I=3`: Beep 3 times with defaults.
- `BEEP I=3 DUR=100`: Beep 3 times, for 100ms each.

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

# LCD RGB
This just provides an easy shortcut to change your neopixel LCD color. This may need modifying depending on your particular LCD. Mine is an MINI12864.

I have my LCD turn red during runouts, and green during filament swaps.

Example usage: `LCDRGB R=0.8 G=0 B=0`

```
[gcode_macro LCDRGB]
gcode:
    {% set r = params.R|default(1)|float %}
    {% set g = params.G|default(1)|float %}
    {% set b = params.B|default(1)|float %}

    SET_LED LED=lcd RED={r} GREEN={g} BLUE={b} INDEX=1 TRANSMIT=0
    SET_LED LED=lcd RED={r} GREEN={g} BLUE={b} INDEX=2 TRANSMIT=0
    SET_LED LED=lcd RED={r} GREEN={g} BLUE={b} INDEX=3
```

To reset the RGB / set the initial RGB. (**set your default LCD colors here**, and use `RESETRGB` to call set it back.)
```
[gcode_macro RESETRGB]
gcode:
    SET_LED LED=lcd RED=1 GREEN=0.45 BLUE=0.4 INDEX=1 TRANSMIT=0
    SET_LED LED=lcd RED=0.25 GREEN=0.2 BLUE=0.15 INDEX=2 TRANSMIT=0
    SET_LED LED=lcd RED=0.25 GREEN=0.2 BLUE=0.15 INDEX=3
```

To set the default colors at startup (required)
```
[delayed_gcode SETDISPLAYNEOPIXEL]
initial_duration: 1
gcode:
    RESETRGB
```

# My Pause/Resume Macros (For Runouts, Filament Swaps, and Manual Pauses)

You need `[pause_resume]` specified in your config to be able to use these.

This macro set's features:

- Moves the toolhead (z hops) up by 10mm, then moves the toolhead to the front for easy loading/unloading.
    - Will not z hop if this exceeds your max Z position.
- Has protections to not allow you to automatically hit pause or resume twice.
- During the pause, allows you to move toolhead around, and even run load/unload filament macros etc. It wil automatically return to its original position before resuming.
- Automatically restores your gcode state (absolute vs relative extrusion mode, etc), should it be changed during the pause by another macro.
- Primes the nozzle while traveling back to resume the print, wiping the excess along the way. This just results in one little string to pick off.
- Sets the idle timeout to 12 hours during the pause, and returns it to your configured value upon resume.
- Turns off your filament sensor during the pause, so it doesn't trip and run its runout gcode again while you're already paused.
- Turns off the hotend during the pause, and turns it back on for the resume.*
    - \* *I highly advise keeping this functionality, even though it's a bit annoying. It's a safety feature. It's not ideal to lave your hotend cooking all night waiting for you to come and swap filament. And with a smart filament sensor, it can even sometimes catch heat creep clogs should your hotend fan fail.*

**Some things are commented out that rely on other macros.** You can uncomment them if you choose to use those other macros.

## M600 (Filament Change) Alias

This allows your pause to work natively with slicers that insert `M600` for color changes. This just calls the pause macro (below).
```
[gcode_macro M600]
gcode:
    #LCDRGB R=0 G=1 B=0  ; Turn LCD green
    PAUSE                ; Pause
```
## Runout G-Code
This goes in your filament sensor config section.
```
runout_gcode:
    #LCDRGB R=1 G=0 B=0  ; Turn LCD red
    PAUSE                ; Pause
    #BEEP I=12           ; Beep 12 times
```

## Pause
If you use a filament sensor, put its name in the `SET_FILAMENT_SENSOR` command. Otherwise, comment that out.

If you want your toolhead to park somewhere other than front center, modify the X/Y coordinates in the last `G1` command.
```
[gcode_macro PAUSE]
rename_existing: BASE_PAUSE
gcode:
    # Parameters
    {% set z = params.Z|default(10)|int %}                                                                                  ; z hop amount
    
    {% if printer['pause_resume'].is_paused|int == 0 %}     
        SET_GCODE_VARIABLE MACRO=RESUME VARIABLE=zhop VALUE={z}                                                             ; set z hop variable for reference in resume macro
        SET_GCODE_VARIABLE MACRO=RESUME VARIABLE=etemp VALUE={printer['extruder'].target}                                   ; set hotend temp variable for reference in resume macro
                                
        SET_FILAMENT_SENSOR SENSOR=filament_sensor ENABLE=0                                                                 ; disable filament sensor       
        SAVE_GCODE_STATE NAME=PAUSE                                                                                         ; save current print position for resume                
        BASE_PAUSE                                                                                                          ; pause print
        {% if (printer.gcode_move.position.z + z) < printer.toolhead.axis_maximum.z %}                                      ; check that zhop doesn't exceed z max
            G91                                                                                                             ; relative positioning
            G1 Z{z} F900                                                                                                    ; raise Z up by z hop amount
        {% else %}
            { action_respond_info("Pause zhop exceeds maximum Z height.") }                                                 ; if z max is exceeded, show message and set zhop value for resume to 0
            SET_GCODE_VARIABLE MACRO=RESUME VARIABLE=zhop VALUE=0
        {% endif %}
        G90                                                                                                                 ; absolute positioning
        G1 X{printer.toolhead.axis_maximum.x/2} Y{printer.toolhead.axis_minimum.y+5} F19500                                 ; park toolhead at front center
        SAVE_GCODE_STATE NAME=PAUSEPARK                                                                                     ; save parked position in case toolhead is moved during the pause (otherwise the return zhop can error) 
        M104 S0                                                                                                             ; turn off hotend
        SET_IDLE_TIMEOUT TIMEOUT=43200                                                                                      ; set timeout to 12 hours
    {% endif %}
```

## Resume
If you use a filament sensor, put its name in the `SET_FILAMENT_SENSOR` command. Otherwise, comment that out.
```
[gcode_macro RESUME]
rename_existing: BASE_RESUME
variable_zhop: 0
variable_etemp: 0
gcode:
    # Parameters
    {% set e = params.E|default(2.5)|int %}
    
    {% if printer['pause_resume'].is_paused|int == 1 %}
        SET_FILAMENT_SENSOR SENSOR=filament_sensor ENABLE=1                                                                 ; enable filament sensor
        #RESETRGB                                                                                                            ; reset LCD color
        SET_IDLE_TIMEOUT TIMEOUT={printer.configfile.settings.idle_timeout.timeout}                                         ; set timeout back to configured value
        {% if etemp > 0 %}
            M109 S{etemp|int}                                                                                               ; wait for hotend to heat back up
        {% endif %}
        RESTORE_GCODE_STATE NAME=PAUSEPARK MOVE=1 MOVE_SPEED=100                                                            ; go back to parked position in case toolhead was moved during pause (otherwise the return zhop can error)  
        G91                                                                                                                 ; relative positioning
        M83                                                                                                                 ; relative extruder positioning
        {% if printer[printer.toolhead.extruder].temperature >= printer.configfile.settings.extruder.min_extrude_temp %}                                                
            G1 Z{zhop * -1} E{e} F900                                                                                       ; prime nozzle by E, lower Z back down
        {% else %}                      
            G1 Z{zhop * -1} F900                                                                                            ; lower Z back down without priming (just in case we are testing the macro with cold hotend)
        {% endif %}                             
        RESTORE_GCODE_STATE NAME=PAUSE MOVE=1 MOVE_SPEED=60                                                                 ; restore position
        BASE_RESUME                                                                                                         ; resume print
    {% endif %}
```

## Cancel

Clears any pause and runs PRINT_END macro.

```
[gcode_macro CANCEL_PRINT]
rename_existing: BASE_CANCEL_PRINT
gcode:
    SET_IDLE_TIMEOUT TIMEOUT={printer.configfile.settings.idle_timeout.timeout} ; set timeout back to configured value
    CLEAR_PAUSE
    SDCARD_RESET_FILE
    PRINT_END
    BASE_CANCEL_PRINT
```

## Octoprint
If you use Octoprint, put these in your "GCODE Script" section to enable the UI buttons to work properly.

- ![](/images/Octoprint-Gcode-Scripts.png)

# Filament Sensor Management
This disables the filament sensor 1 second after startup. This prevents it from tripping while you're just loading filament, doing testing or maintenance, etc.

Put your filament sensor's name after `SENSOR=`.

```
[delayed_gcode DISABLEFILAMENTSENSOR]   
initial_duration: 1
gcode:
    SET_FILAMENT_SENSOR SENSOR=filament_sensor ENABLE=0
```

Then:
- Put `SET_FILAMENT_SENSOR SENSOR=filament_sensor ENABLE=1` in your `PRINT_START`/resume macros.
- Put `SET_FILAMENT_SENSOR SENSOR=filament_sensor ENABLE=0` in your `PRINT_END`/pause/cancel macros. 

The above pause/resume/cancel macros have this already. Just update the sensor name.

# Parking

Park the toolhead at different places. Automatically determined based on your printer's configured size.

```
# Park front center
[gcode_macro PARKFRONT]
gcode:
    CG28                                                                                                                        ; home if not already homed
    SAVE_GCODE_STATE NAME=PARKFRONT
    G90                                                                                                                         ; absolute positioning
    G0 X{printer.toolhead.axis_maximum.x/2} Y{printer.toolhead.axis_minimum.y+5} Z{printer.toolhead.axis_maximum.z/2} F19500        
    RESTORE_GCODE_STATE NAME=PARKFRONT
```
```
# Park front center, but low down.
[gcode_macro PARKFRONTLOW]
gcode:
    CG28                                                                                                                        ; home if not already homed
    SAVE_GCODE_STATE NAME=PARKFRONT
    G90                                                                                                                         ; absolute positioning
    G0 X{printer.toolhead.axis_maximum.x/2} Y{printer.toolhead.axis_minimum.y+5} Z20 F19500                                     
    RESTORE_GCODE_STATE NAME=PARKFRONT
```
```
# Park top rear left
[gcode_macro PARKREAR]
gcode:
    CG28                                                                                                                        ; home if not already homed
    SAVE_GCODE_STATE NAME=PARKREAR
    G90                                                                                                                         ; absolute positioning
    G0 X{printer.toolhead.axis_minimum.x+10} Y{printer.toolhead.axis_maximum.y-10} Z{printer.toolhead.axis_maximum.z-50} F19500     
    RESTORE_GCODE_STATE NAME=PARKREAR
```
```
# Park at center of build volume
[gcode_macro PARKCENTER]
gcode:
    CG28                                                                                                                        ; home if not already homed
    SAVE_GCODE_STATE NAME=PARKCENTER
    G90                                                                                                                         ; absolute positioning
    G0 X{printer.toolhead.axis_maximum.x/2} Y{printer.toolhead.axis_maximum.y/2} Z{printer.toolhead.axis_maximum.z/2} F19500    
    RESTORE_GCODE_STATE NAME=PARKCENTER
```
```
# Park 15mm above center of bed
[gcode_macro PARKBED]
gcode:
    CG28                                                                                                                        ; home if not already homed
    SAVE_GCODE_STATE NAME=PARKBED
    G90                                                                                                                         ; absolute positioning
    G0 X{printer.toolhead.axis_maximum.x/2} Y{printer.toolhead.axis_maximum.y/2} Z15 F19500                                     
    RESTORE_GCODE_STATE NAME=PARKBED
```

# Dump Parameters
This dumps all Klipper parameters to the g-code terminal. This helps to find Klipper system variables for use in macros.
```
[gcode_macro DUMP_PARAMETERS]
gcode:
   {% for name1 in printer %}
      {% for name2 in printer[name1] %}
         { action_respond_info("printer['%s'].%s = %s" % (name1, name2, printer[name1][name2])) }
      {% else %}
         { action_respond_info("printer['%s'] = %s" % (name1, printer[name1])) }
      {% endfor %}
   {% endfor %}
```

# Replace `M109`/`M190` With `TEMPERATURE_WAIT`
Replace `M109` (wait for hotend temperature) and `M190` (wait for bed temperature) with TEMPERATURE_WAIT.

This just makes Klipper resume immediately after reaching temp. Otherwise it waits for the temperature to stabilize.

## M109
```
[gcode_macro M109]
rename_existing: M99109
gcode:
    #Parameters
    {% set s = params.S|float %}
    
    {% if s != 0 %}
        M104 {% for p in params %}{'%s%s' % (p, params[p])}{% endfor %}  ; Set hotend temp
        TEMPERATURE_WAIT SENSOR=extruder MINIMUM={s} MAXIMUM={s+1}       ; Wait for hotend temp (within 1 degree)
    {% endif %}
```

## M190
:warning: If you are using my [bed fans](https://github.com/VoronDesign/VoronUsers/tree/master/printer_mods/Ellis/Bed_Fans) macros, **do not use this version.** Those macros include a variant of this with other essential functions.

```
[gcode_macro M190]
rename_existing: M99190
gcode:
    #Parameters
    {% set s = params.S|float %}
    
    {% if s != 0 %}
        M140 {% for p in params %}{'%s%s' % (p, params[p])}{% endfor %}   ; Set bed temp
        TEMPERATURE_WAIT SENSOR=heater_bed MINIMUM={s} MAXIMUM={s+1}      ; Wait for bed temp (within 1 degree)
    {% endif %}
```