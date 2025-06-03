
"""

https://atcoder.jp/contests/abc173/tasks/abc173_e

クソだけどやろう

正負・0を分割

0がある場合は、最大を0に更新
0がN-K個より多い場合は即終了

残りの場合は、0を取らなくても構成できる場合のみ


"""

import sys
N,K = map(int,input().split())
A = list(map(int,input().split()))

pl = []
mi = []
znum = 0

if K == 1:
    print (max(A))
    sys.exit()

for i in A:
    if i > 0:
        pl.append(i)
    elif i == 0:
        znum += 1
    else:
        mi.append(i)

ans = float("-inf")
if znum > 0:
    ans = 0

#0にならざるを得ない場合を処理
if znum > N-K:
    print (ans)
    sys.exit()

#答えが負になる場合も処理する
#大きいほうからかけていけばいい
#N個の場合 or 正がない場合は負になりえない
mod = 10**9+7
pl.sort()
mi.sort()

if K == N:
    ans = 1
    for i in range(N):
        ans *= A[i]
        ans %= mod
    print (ans)
    sys.exit()

if K % 2 == 1 and len(pl) == 0:
    if znum > 0:
        ans = 0
    else:
        ans = 1
    mi.reverse()
    for i in range(K):
        ans *= mi[i]
        ans %= mod
    print (ans)
    sys.exit()

#まず、2個づつセットにすることを考える
#正負でセットにしていって、あまり同士も合成する

if K % 2 == 1:
    K -= 1
    ans = pl[-1]
    del pl[-1]
else:
    ans = 1

pl2 = []
pl.reverse()
if len(pl) % 2 == 1:
    pl.append(0)
if len(mi) % 2 == 1:
    mi.append(0)
for i in range(0,len(pl),2):
    pl2.append(pl[i] * pl[i+1])
for i in range(0,len(mi),2):
    pl2.append(mi[i] * mi[i+1])


pl2.sort()
pl2.reverse()
for i in range(K//2):
    ans *= pl2[i]
    ans %= mod
print (ans)