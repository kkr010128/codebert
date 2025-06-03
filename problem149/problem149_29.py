N, M, X = map(int, input().split())

book = [0] + [list(map(int, input().split())) for _ in range(N)]
ans = N * 10**5 + 1

for i in range(2**N):
    read = [0] * (N+1)
    rikai = [0] * (M+1)
    cost = 0
    for j in range(N):
        read[j+1] = i%2
        i //= 2
    for j in range(1, N+1):
        if read[j] == 1:
            cost += book[j][0]
            for k in range(1, M+1):
                rikai[k] += book[j][k]
    
    if min(rikai[1:]) >= X:
        ans = min(ans, cost)

print(ans if ans != (N * 10**5 + 1) else -1)
