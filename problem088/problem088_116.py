N = int(input())
A = list(map(int,input().split()))

minm = A[0]
ans = 0
for i in range(1,N):
    if A[i] < minm:
        ans += minm - A[i]
    if A[i] > minm:
        minm = A[i]
        
print(ans)