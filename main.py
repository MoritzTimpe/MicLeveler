from __future__ import print_function
import os


def calc(percent):
    #wanted 45
    one_percent = 65536 / 100
    return (int(one_percent) * int(percent))

def main():
    filesize = os.path.getsize("level.cfg")

    if filesize == 0:
        f = open('level.cfg', 'w+')
        raw_lvl = input("Input wish percentage: ")
        lvl = calc(raw_lvl)
        f.write(str(raw_lvl))
        f.close()
    else:
        f = open('level.cfg', 'r+')
        lvl = calc(f.read())
    os.system(f"nircmdc.exe 250 setsysvolume {lvl} default_record")
    #          nircmdc.exe loop /number of loops/ /time in ms to execute one loop/ setsysvolume /65536 == 100%/ /device/


if __name__ == "__main__":
    main()