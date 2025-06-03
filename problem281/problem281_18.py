def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 2 * 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

X, Y = map(int, input().split())
#(1, 2)の回数をn, (2, 1)の回数をmとする。
n = (-X + 2 * Y) / 3
m = (-Y + 2 * X) / 3
#いけない場合を除外
if n % 1 != 0:
  print(0)
  quit()
elif m % 1 != 0:
  print(0)
  quit()
#n + m C nで答え  
ans = cmb(int(n + m), int(n), p)
print(ans)


