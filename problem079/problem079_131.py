from math import factorial as fact

S = int(input())
MOD = 10**9+7

ans = 0
for i in range(1,S):
    if S < 3*i : break
    n = S-3*i+i-1
    r = i-1
    ans += fact(n) // (fact(r) * fact(n-r))


print(ans%MOD)