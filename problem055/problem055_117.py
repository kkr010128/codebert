#!/usr/bin/env python3
# -*- coding: utf-8 -*-

B = 4
F = 3
R = 10
SHARPS = 20

def main():
    """
    The function to be called when this script is run as a script.
    
    """
    
    info_number = int(input())
    given_info_str = (info.split() for info in (
        input() for _ in range(info_number)))
    given_info_int = (list(map(int, info)) for info in given_info_str)
    houses = [[[0 for i in range(R)] for j in range(F)] for k in range(B)]
    for info in given_info_int:
        houses[info[0] - 1][info[1] - 1][info[2] - 1] += info[3]
    for num, building in enumerate(houses):
        for floor in building:
            print (" " + " ".join(map(str, floor)))
        if num < (B - 1):
            print("#" * 20)

if __name__ == "__main__":
    main()