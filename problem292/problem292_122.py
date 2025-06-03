import math 
import itertools

n = int(input())
d = list(map(int, input().split()))
ans = 0
for i in itertools.permutations(d, 2):
    ans += i[0] *i[1]
print(ans //2)        