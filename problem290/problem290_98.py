import math
N,K = map(int,input().split())
A = sorted(list(map(int,input().split())))
F = sorted(list(map(int,input().split())),reverse=True)
high = 0
for i in range(N):
    high = max(high,A[i]*F[i])
low = -1
while high-low>1:
    mid = (high+low)//2
    flag = 1
    T = K
    for i in range(N):
        if A[i]*F[i]<=mid:continue
        else:
            T -= math.ceil(A[i]-mid/F[i])
            if T<0:
                flag = 0
                break
    if flag==1:
        high = mid
    else:
        low = mid
print(high)