N = int(input())
A = list(map(int,input().split()))
ans = 0
for i in range(N-1):
    next = i + 1
    if A[i] > A[next]:
        a =A[i] - A[next]
        ans += a
        A[next] += a
    else:
        pass
print(ans)
