# microbit

## Flashing the Microbit firmware

-  [Version 0249 for Microbit V1](0249_microbit_firmware.hex)
-  [Instructions](https://microbit.org/get-started/user-guide/firmware/)

## Micropython for Microbit

- [API Documentation](https://microbit-micropython.readthedocs.io/en/v1.0.1/)
- [Using uflash](https://uflash.readthedocs.io/en/latest/index.html)

### Flashing Micropython for the first time

```Flashing Python to: /run/media/edrdo/MICROBIT/micropython.hex
$ uflash

$ minicom -D /dev/ttyACM0  # Set device appropriately and hit Control+C once connected
Welcome to minicom 2.7.1

OPTIONS: I18n 
Compiled on Jul 28 2020, 00:00:00.
Port /dev/ttyACM0, 17:25:18

Press CTRL-A Z for help on special keys
>>> help()
Welcome to MicroPython on the micro:bit!

Try these commands:
  display.scroll('Hello')
  running_time()
  sleep(1000)
  button_a.is_pressed()
What do these commands do? Can you improve them? HINT: use the up and down
arrow keys to get your command history. Press the TAB key to auto-complete
unfinished words (so 'di' becomes 'display' after you press TAB). These
tricks save a lot of typing and look cool!

Explore:
Type 'help(something)' to find out about it. Type 'dir(something)' to see what
it can do. Type 'dir()' to see what stuff is available. For goodness sake,
don't type 'import this'.

Control commands:
  CTRL-C        -- stop a running program
  CTRL-D        -- on a blank line, do a soft reset of the micro:bit
  CTRL-E        -- enter paste mode, turning off auto-indent

For a list of available modules, type help('modules')

For more information about Python, visit: http://python.org/
To find out about MicroPython, visit: http://micropython.org/
Python/micro:bit documentation is here: https://microbit-micropython.readthedocs.io/
```

### Flashing any program

```
uflash script.py
```
