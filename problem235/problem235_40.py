from collections import Counter
N = int(input())
A = list(map(int,input().split()))
memo = []
for i in range(N):
    tmp = []
    a = A[i]
    d = 2
    while d*d <= a:
        while a%d == 0:
            tmp.append(d)
            a //= d
        d += 1
    if a!=1:
        tmp.append(a)
    memo.append(Counter(tmp))

lcm = Counter([])

for count in memo:
    for k,v in count.items():
        if k not in lcm:
            lcm[k] = v
        else:
            lcm[k] = max(lcm[k],v)
mod = 10**9 +7
LCM = 1
for k,v in lcm.items():
    LCM = LCM*pow(k,v)%mod

ans = 0
for a in A:
    ans = (ans + LCM*pow(a,mod-2,mod))%mod
print(int(ans))