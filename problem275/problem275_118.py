X, Y = [int(_) for _ in input().split()]

ans = 0
V = [400000, 300000, 200000, 100000]
if X <= 3:
    ans += V[X]
if Y <= 3:
    ans += V[Y]
if X == Y == 1:
    ans += V[0]

print(ans)
