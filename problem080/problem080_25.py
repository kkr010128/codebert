import numpy as np
# import math
# import copy
# from collections import deque
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10000)


def main():
    N = int(input())
    xy = [list(map(int,input().split())) for i in range(N)]

    z_max = 0
    z_min = 2 * 10 **9

    w_max = - 10 ** 9
    w_min = 10 ** 9

    for i in range(N):
        z = xy[i][0] + xy[i][1]
        w = xy[i][0] - xy[i][1]
        z_max = max(z_max,z)
        z_min = min(z_min,z)
        w_max = max(w_max,w)
        w_min = min(w_min,w)

    res = max(z_max-z_min,w_max-w_min)

    print(res)



main()
