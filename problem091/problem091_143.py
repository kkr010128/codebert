from itertools import combinations
n = int(input())
l = list(map(int, input().split()))
comb = list(combinations(range(n), 3))
ans = 0
for i,j,k in comb:
    a = l[i]
    b = l[j]
    c = l[k]

    if a == b:
        continue
    if b == c:
        continue
    if c == a:
        continue
    if sum([a,b,c]) <= 2 * max(a,b,c):
        continue
    ans += 1
print(ans)
