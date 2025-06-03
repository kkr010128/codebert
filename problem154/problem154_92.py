N, K = map(int, input().split())
d = []
A = []
for i in range(K):
    d.append(int(input()))
    A.append(list(map(int, input().split())))

sunuke = [0] * N
for i in range(K):
    for j in range(d[i]):
        sunuke[A[i][j] - 1] += 1

ans = 0
for i in range(N):
    if sunuke[i] == 0:
        ans += 1

print(ans)
