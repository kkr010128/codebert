
N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

MAX = 10**10 + 10

# Ai+Ajを列挙して大きいほうからM番目となるスコアSを求める
# その後S以上となるスコアを加算して合計値を求める

from bisect import bisect_left

def judge(x,key):
    # スコアx以上となるのがkey個以上あるか？
    
    num = 0
    
    for i in range(N):
        eidx = bisect_left(A,x-A[i])
        num += N-eidx
    
    if num >= key:
        return True
    else: 
        return False


def meguru(key):
    ok = -1
    ng = MAX
    
    while (abs(ok-ng)>1):
        mid = (ok+ng)//2
        if judge(mid,key):
            ok = mid
        else:
            ng = mid
    return ok


D = meguru(M)
ans = 0

ruisekiwa = [0]*(N+1)
for i in range(N):
    ruisekiwa[i+1] = ruisekiwa[i] + A[i]

num = 0

for i in range(N):
    eidx = bisect_left(A,D+0.5-A[i])
    ans += A[i] * (N-eidx)
    ans += ruisekiwa[N] - ruisekiwa[eidx]
    num += N-eidx

if num<M:
    ans += (M-num)*D

print(ans)
    


