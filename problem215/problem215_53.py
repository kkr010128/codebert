N, K = map(int, input().split())

def createFacArr(n, mod):
    '''
    二項係数計算用の配列の作成

    Parameters
    n : int
        配列のサイズ
    mod : int
        あまり

    Returns
    fac : list
        階乗のリスト
    finv : list
        modの逆元のリスト
    ivn : list
    '''
    fac = [0] * n
    finv = [0] * n
    inv = [0] * n
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, n):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod%i] * (mod // i) % mod
        finv[i] = finv[i-1] * inv[i] % mod
    return fac, finv

def comb(n ,k, mod, fac, finv):
    '''
    二項係数の計算

    Parameters
    n : int
        元集合
    k : int
        元集合から選択する数
    mod : int
        あまり
    fac : list
        階乗のリスト
    finv : list
        逆元のリスト
    
    Returns
    c : int
        nCkの組み合わせの数
    '''
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

K = min(N-1, K)
ans = 0
MOD = 10 ** 9 + 7
fac, finv = createFacArr(N+100, MOD)

for i in range(K+1):
    # iは0の個数
    ans += comb(N, i, MOD, fac, finv) * comb(N-1, N-i-1, MOD, fac, finv) % MOD
    ans %= MOD
print(ans)
