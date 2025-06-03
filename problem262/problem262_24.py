N = int(input())
T = [[] for _ in range(N)]
for i in range(N):
    A = int(input())
    for j in range(A):
        x, y = map(int, input().split())
        x -= 1
        T[i].append((x, y))

ans = 0
for i in range(1 << N):
    isPossible = True
    bit = [0] * N
    for k in range(N):
        if (i >> k) & 1:
            bit[k] = 1
    for idx, b in enumerate(bit):
        if b == 1:
            for x, y in T[idx]:
                isPossible &= (bit[x] == y)
    if isPossible:
        ans = max(ans, bit.count(1))
print(ans)
