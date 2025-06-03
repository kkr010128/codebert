
"""
方針：

幸福度が一定以上のつなぎ方の数→NlogNで二分探索可能
採用するうち最小の幸福度を NlogNlogNで探索

累積和を用いて合計を算出

2 3
5 2

10 + 7 + 7 = 24

"""

import bisect

def wantover(n): #n以上の幸福度のつなぎ方の数がM以上ならTrueを返す

    ret = 0

    for i in range(N):

        serchnum = n - A[i]

        ret += (N - bisect.bisect_left(A,serchnum))

    #print ("over",n,"is",ret)

    if ret >= M:
        return True
    else:
        return False


N,M = map(int,input().split())

A = list(map(int,input().split()))
A.sort()

#print (wantover(7))

hpl = 0
hpr = A[-1] * 2 + 1

while hpr - hpl != 1:

    mid = (hpr + hpl) // 2

    if wantover(mid):

        hpl = mid

    else:

        hpr = mid

#ここで最小の幸福度はhpl
#print (hpl,hpr)

B = [0] #累積和行列

for i in range(N):

    B.append(B[-1] + A[-1 - i])

#print (A)
#print (B)

ans = 0
plnum = 0 #つないだ手の回数
for i in range(N):

    i = N-i-1

    ind = bisect.bisect_left(A,hpl - A[i])

    #print (hpl,A[i],N-ind)
    
    plnum += N - ind
    
    ans += B[N - ind] + A[i] * (N-ind)

#print (ans,plnum)
print (ans - hpl * (plnum - M))
        
