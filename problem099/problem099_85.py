N,K = list(map(int,input().split()))
A = list(map(int,input().split()))
 
NG=0
OK=max(A)+1
 
while OK-NG>1:
    mid = (OK+NG)//2
    cur=0
    for x in A:
        cur += (x-1)//mid
    if cur > K:
        NG=mid
    else:
        OK=mid
print(OK)