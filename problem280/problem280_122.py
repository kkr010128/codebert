import math
import itertools
n = int(input())
al = [0] * n
bl = [0] * n
for i in range(n):
    al[i], bl[i] = map(int, input().split())
bunbo = math.factorial(n)
ans = 0
for p in itertools.permutations(list(range(n))):
    for i in range(n-1):
        ans += ((al[p[i+1]]-al[p[i]])**2+(bl[p[i+1]]-bl[p[i]])**2)**0.5
print(ans/bunbo)
