N, K = map(int, input().split())
ans = 0

for height in map(int, input().split()):
    if height >= K:
        ans += 1

print(ans)
