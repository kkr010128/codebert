# -*- coding: utf-8 -*-
import sys


def main():
    N = int( sys.stdin.readline() )
    c_list = list(sys.stdin.readline().rstrip())
    

    cnt = 0
    L = 0
    R = len(c_list) - 1

    while L < R:
        if (c_list[L] == "W") and (c_list[R] == "R"):
            c_list[L], c_list[R] = c_list[R], c_list[L]
            cnt += 1
            L += 1
            R -= 1
        elif c_list[L] == "R":
            L += 1
        elif c_list[R] == "W":
            R -= 1
    
    
    print(cnt)


if __name__ == "__main__":
    main()
