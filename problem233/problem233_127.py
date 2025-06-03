n = int(input())
P = list(map(int, input().split()))

ans = 0
prev_min = P[0]
for p in P:
    if prev_min >= p:
        ans += 1
        prev_min = p
print(ans)