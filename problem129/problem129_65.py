N = int(input())
A = sorted(list(map(int, input().split())))

#篩
M = 10**6+ 10
c = [0] * M
for i in range(N):
    if c[A[i]-1] >= 1:
        c[A[i]-1] = c[A[i]-1] + 1
    else:
        for j in range(1, M//A[i] + 1):
            c[A[i]*j-1] += 1

#チェック
ans = 0
for i in range(N):
    if c[A[i]-1] <= 1:
        ans += 1

print(ans)
