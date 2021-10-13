from __future__ import print_function
import os

def calc(percent):
    one_percent = 65536 / 100
    return (one_percent * percent)

def main():
    percent = calc(int(input("Input wish percentage: ")))
    os.system(f"nircmdc.exe loop 144000 250 setsysvolume {percent} default_record")
    #          nircmdc.exe loop /number of loops/ /time in ms to execute one loop/ setsysvolume /65536 == 100%/ /device/


if __name__ == "__main__":
    main()