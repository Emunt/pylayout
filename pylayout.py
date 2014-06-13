#!/usr/bin/python3

import lib.windowmanager as wm

def main():
    w = wm.Window('Ubuntu Start Page - Mozilla Firefox', 0, 0, 500, 500)
    w.update()
    w.setxywh(500,500,500,500)

if __name__ == '__main__':
    main()
