
mod = 10**9+7
MAX_N = 10 ** 6

fact = [1]
fact_inv = [0] * (MAX_N + 4)
for i in range(MAX_N + 3):
    fact.append(fact[-1] * (i + 1) % mod)

fact_inv[-1] = pow(fact[-1], mod - 2, mod)
for i in range(MAX_N + 2, -1, -1):
    fact_inv[i] = fact_inv[i + 1] * (i + 1) % mod

def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod

OK = False
X, Y = map(int, input().split())
for i in range(0, max(X, Y)+1):
    if (Y - (X - i*2)*2) == i and X-2*i >= 0:
        x = i
        y = X - i*2
        print(mod_comb_k(x + y, min(x, y), mod))
        OK = True
        break
if not OK:
    print(0)