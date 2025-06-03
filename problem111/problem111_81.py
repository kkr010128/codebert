N = int(input())
*A, = map(int, input().split())
A.sort(reverse=True)
k = (N+1)//2

ans = sum(A[0:k])*2-A[0]
if N & 1:
    ans -= A[k-1]
print(ans)
