n,k = map(int,input().split())
A = [int(i) for i in input().split()]
A.sort()
F = [int(i) for i in input().split()]
F.sort(reverse=True)

left = -1
right = 10**12
def f(x): return sum(max(A[i]-x//F[i],0) for i in range(n)) <= k
    
while right - left > 1:
    mid = (left+right)//2
    if f(mid): right = mid
    else: left = mid
print(right)