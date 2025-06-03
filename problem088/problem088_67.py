N = int(input())
As = list(map(int, input().split()))

h = 0
ans = 0

for i in range(N):
    h = max(h, As[i])
    ans += h - As[i]

print(ans)
