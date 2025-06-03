import numpy as np
N,K = map(int,input().split())
import math
A = list(map(int,input().split()))
flag = 0
if 0 in A:
    flag = 1
A.sort()

plus = list(filter(lambda x:x>0, A))[::-1]
plus = list(map(lambda x:np.longdouble(math.log(x,10000000)),plus))
from itertools import accumulate
acc_plu = [0] +  list(accumulate(plus))
minu = filter(lambda x:x<0, A)
minu = list(map(lambda x:np.longdouble(math.log(-x,10000000)),minu))
acc_min = [0] +  list(accumulate(minu))


if K % 2 == 0 : num = K // 2 + 1
else: num = (K + 1) // 2 
cand = []
x = K
y = 0
MOD = 10**9 +7
for i in range(num):
    try:
        cand.append((acc_plu[x] +  acc_min[y],x ,y ))
    except: pass
    x -= 2 
    y += 2

ans = 1
if cand == []:
    if flag:
        print(0)
        exit()
    cnt = 0
    #マイナス確定
    abss = sorted(list(map(lambda x :abs(x),A)))
    for x in abss:
        if cnt == K:break
        ans *= x
        ans %= MOD
        cnt += 1
    ans *= -1
    ans %= MOD
    print(ans)
else:
    cand = sorted(cand)[::-1]
    plus = list(filter(lambda x:x>0, A))[::-1]
    minu = list(filter(lambda x:x<0, A))
    c = cand[0]
    ans = 1
    for i in range(c[1]):
        ans *= plus[i]
        ans %= MOD
    for i in range(c[2]):
        ans *= minu[i]
        ans %= MOD
    print(ans)

