from math import gcd
n = int(input())
s = list(map(int, input().split()))
s.sort()
dp = [0] * ((10 ** 6) + 100)

res = s[0]
for ss in s:
    dp[ss] += 1
    res = gcd(res, ss)

A = max(s)
pairwise = True
setwise = (res == 1)

primes = set(range(2, A+1))
for i in range(2, int(A**0.5+1)):
    if i not in primes:
        i += 1
    else:
        ran = range(i*2, A+1,i)
        primes.difference_update(ran)
primes = list(primes)

for i in primes:
    cnt = 0
    for j in range(i, A + 1, i):
        cnt += dp[j]
    if cnt > 1:
        pairwise = False
        break

if pairwise:
    print("pairwise coprime")
elif setwise:
    print("setwise coprime")
else:
    print("not coprime")
