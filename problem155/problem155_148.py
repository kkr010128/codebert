N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
good = [True]*N
for _ in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    if H[a] >= H[b]:
        good[b] = False
    if H[a] <= H[b]:
        good[a] = False
print(good.count(True))
