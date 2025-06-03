N = int(input())
A = list(map(int, input().split()))

b = [0] * (N+1)
b[0] = 1
flag = True

for i in range(N):
    if A[i] > b[i]:
        flag = False

    b[i+1] = (b[i] - A[i]) * 2

if A[N] > b[N]:
    flag = False
ans = 0
l = 0
for i in range(N, -1, -1):
    l += A[i]
    ans += min(l, b[i])

if flag:
    print(ans)
else:
    print(-1)

