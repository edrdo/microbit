#! /usr/bin/python3
import serial
import sys


def main():
    # todo set serial port from args
    serialPort = serial.Serial(
        sys.argv[1], baudrate=115200, timeout=3.0)

    count = 0
    while True:
        data = {}

        try:
            serialBytes = serialPort.readline()
            data = serialBytes.decode('Ascii')
        except KeyboardInterrupt:
            break
        except:
            print("uart data error")
            continue
        print(data)


if __name__ == "__main__":
    main()
