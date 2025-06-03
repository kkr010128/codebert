#　解説確認後
#　参考サイト「けんちょんの競プロ精進記録」
#　URL: https://atcoder.jp/contests/abc142/tasks/abc142_d

import math
def prime_factorize(n): # 素因数分解
    p = 2
    res = []
    while p*p <= n:
        if n % p: # 割り切れない
            p += 1
            continue
        num = 0
        while n % p == 0:
            n //= p
            num += 1
        res.append((p,num))
        p += 1
    if n != 1: res.append((n,1))
    return res

a,b = map(int,input().split())

G = math.gcd(a,b) # 最大公約数

pl = prime_factorize(G)

print(len(pl)+1) # 1+n個なので