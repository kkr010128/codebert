from math import gcd

from math import factorial as f

from math import ceil, floor, sqrt
import math

import bisect
import re
import heapq

from copy import deepcopy
import itertools
from itertools import permutations

from sys import exit

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

yes = "Yes"
no = "No"


def main():
    n, x, t = mi()
    tmp = 0
    ans = 0
    for i in range(10000):
        ans += t
        tmp += x
        if n <= tmp:
            break
    print(ans)


main()
