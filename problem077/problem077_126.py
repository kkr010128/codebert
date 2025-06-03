import sys
from functools import reduce


def input():
    return sys.stdin.readline()[:-1]


a, b, c, d = map(int, input().split())
ans1 = a * c
ans2 = b * d
ans3 = b * c
ans4 = a * d
print(max([ans1, ans2, ans3, ans4]))
