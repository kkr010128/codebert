# Trick or Treat

N, K = map(int, input().split())
count = [0] * N
for _ in range(K):
    d = int(input())
    treat = list(map(int, input().split()))
    for val in treat:
        count[val-1] += 1

ans = 0
for i in range(N):
    if count[i] == 0:
        ans += 1

print(ans)

