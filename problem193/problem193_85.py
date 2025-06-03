import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    if len(x) == 0:
        return []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa != x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False
"""
def nibu(x,n,r):
    ll = 0
    rr = r
    while True:
        mid = (ll+rr)//2

    if rr == mid:
        return ll
    if (ここに評価入れる):
        rr = mid
    else:
        ll = mid+1
"""

h,w,k = m()

s = []

for i in range(h):
    s.append(list(map(int,input()[:-1])))

st = [0 for i in range(h)]
dp = [[0,0] for i in range(h)]
ans = mod

for po in range(2 << h):
    de = 0
    tm = 0
    for j in range(h):
        dp[j][0] = 0
        dp[j][1] = 0
    for j in range(h):
        if j == 0:
            st[0] = 0
        else:
            a = (po>>j)&1
            b = (po>>(j-1))&1
            if a != b:
                de += 1
            st[j] = de
            
    tm += de
    
    for kp in range(w):
        fl = 0
        for kk in range(h):
            if s[kk][kp] == 1:
                dp[st[kk]][1] += 1
        if all(dp[x][0] + dp[x][1] <= k for x in range(h)):
            for kk in range(h):
                dp[kk][0] += dp[kk][1]
                dp[kk][1] = 0
        else:
            tm += 1
            for kk in range(h):
                if dp[kk][0] > k:
                    fl = 1
                    break
                dp[kk][0] = dp[kk][1]
                dp[kk][1] = 0
        if fl:
            break
    else:
        ans = min(tm,ans)
print(ans)








