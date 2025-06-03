N = int(input())
A = list(map(int, input().split()))
ans = 1000
for i in range(N - 1):
    a = A[i]
    if a < A[i + 1]:
        units = ans // a
        ans = (ans - units * a) + units * A[i + 1]
    # print(i, ans)

print(ans)
