def prepare(n, MOD):
    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
     
    return factorials, invs

x, y = map(int,input().split())
if x > 2*y or y > 2*x or (x+y) % 3 != 0:
    print(0)
    exit()

d = (x+y)//3
MOD = 10**9+7
f, i = prepare(10**6, MOD)
nx = (2*y-x) // 3
print(f[d] * i[nx] % MOD * i[d-nx] % MOD)