from _collections import deque
from _ast import Num


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def gw():
    global input_parser
    return next(input_parser)


def gi():
    data = gw()
    return int(data)


MOD = int(1e9 + 7)

import numpy
from collections import deque
from math import sqrt
from math import floor
# https://atcoder.jp/contests/abc145/tasks/abc145_e
#E - All-you-can-eat
"""

"""

N = gi()
M = gi()
S = gw()

lis = [0] * (N + 5)

li = 0

all_good = 1

for i in range(1, N + 1):
    while (i - li > M or (li < i and S[li] == "1")):
        li += 1
    if li == i:
        all_good = 0
        break
    lis[i] = li

if all_good:
    ans = []
    ci = N
    while ci > 0:
        step = ci - lis[ci]
        ans.append(step)
        ci -= step
    ans.reverse()
    for a in ans:
        print(a, end=" ")
else:
    print(-1)
