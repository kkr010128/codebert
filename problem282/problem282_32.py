N, T = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

Dp = [0 for _ in range(T+1)]

ab = sorted(ab, key = lambda x: x[0])

for i in range(N):
    for j in range(T-1,-1, -1):
        if j+ab[i][0] <= T-1:
            kari2 = Dp[j] + ab[i][1]
            if  Dp[j+ab[i][0]] < kari2:
                Dp[j+ab[i][0]] = kari2
        else:
            kari2 = Dp[j] +ab[i][1]
            if Dp[T] < kari2:
                Dp[T] = kari2
                
print(max(Dp))