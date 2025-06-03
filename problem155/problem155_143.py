
N, M = map(int, input().split())
H = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(M)]

ok = [True] * (N + 1)
for a, b in X:
    ok[a] &= H[a - 1] > H[b - 1]
    ok[b] &= H[a - 1] < H[b - 1]

print(sum(ok[1:]))
