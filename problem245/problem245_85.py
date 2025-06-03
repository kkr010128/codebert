import sys
from itertools import combinations
import math


def I(): return int(sys.stdin.readline().rstrip())


def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def S(): return sys.stdin.readline().rstrip()


def LS(): return list(sys.stdin.readline().rstrip().split())


n = I()
s = S()
# print(s.count('ABC'))
ans = 0
for i in range(len(s)-2):
    if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
        ans += 1
print(ans)
