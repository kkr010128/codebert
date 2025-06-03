ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n,p = mi()
s = input()
srev = s[::-1]

if p == 2 or p == 5:
    ans = 0
    for i in range(n):
        if int(s[i]) % p == 0:
            ans += i +1
    print(ans)
    exit()

acum = []
from collections import defaultdict
d = defaultdict(lambda :0)
d = [0] * p
num = 0
tenpow = 1
for i in range(0,n):
    a = int(srev[i])
    a = num + a *tenpow 
    tenpow = tenpow * 10 % p
    modd = a % p
    num = modd
    d[modd] += 1
    acum.append((modd,d[modd]))
ans = d[0]
for i in range(n):
    ans += d[acum[i][0]] - acum[i][1]
print(ans)

