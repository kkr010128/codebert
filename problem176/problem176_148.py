import math

n, k = map(int, input().split())

dic = {} #ここに結果を保存していく。
ans = 0
moddo = 10**9+7

for i in range(k):
    t = k - i #これで大きいほうから順にとる。
    if t > k/2: #tがk/2より大きいときはすべてtじゃないと最大公約数はtにならない。
        dic[t] = 1
        ans += t
    else:
        temp = pow(k//t,n,moddo)
        #print(temp)
        fac = 2
        while fac*t <= k:
            temp -= dic[fac*t]
            fac += 1
        dic[t] = temp%moddo
        ans = (ans+((temp*t)%moddo))%moddo

print(ans)