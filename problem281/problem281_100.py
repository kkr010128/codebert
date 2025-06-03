
from functools import reduce
def comb(n, max_k, mod):
    """
    (n,k) := n個からk個選ぶ組み合わせ
    k = 0~max_Kまでを計算して返す
    """
    res = [1]*(max_k+1)
    t = 1
    for i in range(max_k+1):
        res[i] *= t
        t *= n-i
        t %= mod

    n = reduce(lambda x,y: (x*y)%mod, range(1,max_k+1), 1)
    n = pow(n, mod-2, mod)

    for i in reversed(range(max_k+1)):
        res[i] *= n
        res[i] %= mod
        n *= i
        n %= mod
    return res

X,Y = map(int,input().split())

d = X+Y

if d%3 != 0:
    print(0)
else:
    n = d//3
    if X < n or 2*n < X:
        res = 0
    else:
        res = comb(n,X-n, 10**9+7)[X-n]
    print(res)
