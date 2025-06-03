N, K = [int(x) for x in input().split()]
H = [int(x) for x in input().split()]

ans = 0
for h in H:
    if h >= K:
        ans += 1
print(ans)

