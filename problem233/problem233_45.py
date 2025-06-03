N = int(input())
P = list(map(int, input().split()))
mi = 202020
ans = 0
for p in P:
    if p < mi:
        ans += 1
        mi = p
print(ans)
