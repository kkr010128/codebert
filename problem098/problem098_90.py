# -*- coding: utf-8 -*-
import sys


def main():
    N = int( sys.stdin.readline() )
    c_list = list(sys.stdin.readline().rstrip())
    

    num_R = c_list.count("R")
    cnt = 0

    for i in range(num_R):
        if c_list[i] == "W":
            cnt += 1
    
    print(cnt)


if __name__ == "__main__":
    main()
