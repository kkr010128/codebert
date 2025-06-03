N = int(input())
A = list(map(int, input().split()))
left = 0
SUM = sum(A)
res = SUM
for i in range(N):
    left += A[i] 
    res = min(res,abs(2*left-SUM))
print(res)