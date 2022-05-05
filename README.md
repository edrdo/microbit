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

$ minicom -D /dev/ttyACM0
Welcome to minicom 2.7.1

OPTIONS: I18n 
Compiled on Jul 28 2020, 00:00:00.
Port /dev/ttyACM0, 17:25:18

Press CTRL-A Z for help on special keys


>>> import sys   
>>> print(sys.version)
3.4.0
```

### Flashing any program

```
uflash script.py
```
