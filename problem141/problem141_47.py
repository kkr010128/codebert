N = int(input())
A = list(map(int, input().split()))

rng = [[A[N], A[N]]]

for i in range(N - 1, -1, -1):
    merged = (rng[-1][0] + 1) // 2 + A[i]
    nonmerged = rng[-1][1] + A[i]
    rng.append([merged, nonmerged])
if rng[-1][0] > 1:
    print(-1)
    exit()
rng.reverse()
prev_non_leaf = 1
ans = 1
for i in range(1, N + 1):
    _, u = rng[i]
    ans += min(prev_non_leaf * 2, u)
    prev_non_leaf = prev_non_leaf * 2 - A[i]
print(ans)
