n,k = map(int,input().split())
L = list(map(int,input().split()))

def A(x):
    cnt = 0
    for i in range(n):
        if L[i]%x == 0:
            cnt +=L[i]//x-1
        else:
            cnt +=L[i]//x
    return cnt <= k

lower = 0
upper = max(L)

while upper - lower > 1:
    mid = (lower + upper)//2
    if A(mid):
        upper = mid
    else:
        lower = mid

print(upper)