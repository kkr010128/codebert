def mod_comb_k(n, k, p):
    """二項係数 0(1)

    Args:
        n (int): 添字
        k (int): 添字
        p (int): 除数

    Returns:
        int: nCk mod p
    """
    if n < k or n < 0 or k < 0:
        return 0
    else:
        return fact[n] * fact_inv[k] * fact_inv[n-k] % p

def com_init(n, p):
    """二項係数の計算の前処理 O(N)

    Args:
        n (int): 上限値
        p (int): 除数
    """
    for i in range(n):
        fact.append(fact[-1] * (i+1) % p)

    fact_inv[-1] = pow(fact[-1], p-2, p)
    for i in range(n-1, -1, -1):
        fact_inv[i] = fact_inv[i+1] * (i+1) % p


s = int(input())

mod = 10 ** 9 + 7

fact = [1]
fact_inv = [0] * (s+1)
com_init(s, mod)

res = 0
for i in range(1, s//3+1):
    res = (res + mod_comb_k(s-i*2-1, i-1, mod)) % mod

print(res)