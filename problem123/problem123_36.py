ma = lambda :map(int,input().split())
ni = lambda:int(input())
import collections
import math
import itertools
gcd = math.gcd

n = ni()
A = list(ma())
tot = 0
for a in A:
    tot = tot^a
ans = []
for a in A:
    ans.append(tot^a)
print(*ans)
