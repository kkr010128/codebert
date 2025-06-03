from collections import defaultdict
import itertools

N = int(input())

L = list(map(int, input().split()))

dic = defaultdict(int)

for num in L:
    dic[num] += 1

set_L = set(L)

comb = list(itertools.combinations(set_L, 3))

ans = 0
for a,b,c in comb:
    if a+b <= c or b+c<=a or c+a <= b: continue
    ans += dic[a] * dic[b] * dic[c]

print(ans)
