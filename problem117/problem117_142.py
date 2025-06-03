n,m,k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if sum(A)+sum(B)<=k:
    print(n+m)
    exit()

for i in range(1,n):
    A[i] += A[i-1]
for i in range(1,m):
    B[i] += B[i-1]

from bisect import bisect_right
ans = bisect_right(B,k)
for i in range(n):
    if A[i]>k:
        break
    ans = max(ans, i+1+bisect_right(B,k-A[i]))
print(ans)