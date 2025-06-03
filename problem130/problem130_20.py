import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy


if __name__ == "__main__":
    s = input()
    ans = ""
    for i in range(3):
        ans += s[i]
    print(ans)