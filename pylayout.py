#!/usr/bin/python3

import lib.windowmanager as wm

def main():
    list = wm.OpenWindowList()
    for l in list.list:
        print(l.name)
if __name__ == '__main__':
    main()
