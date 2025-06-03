# a^n mod p
def exp_by_sq(a, n, p):
    if n == 0:
        exp = 1
    elif n == 1:
        exp = a % p
    elif  n % 2 == 0:
        exp = exp_by_sq(a * a % p, n // 2, p)
    else:
        exp = a * exp_by_sq(a * a % p, (n - 1) // 2, p) % p
    return exp % p

# 入力
n, k = [int(x) for x in input().split()]

p = 10 ** 9 + 7
# Find n * sum_{j = 0..m}{(n choose j)^2 * (n - j)}
m = min(n, k)
# 最初の2項
binom = n # n choose 1  mod p
ans = n * ((n * n - n + 1) % p) % p  # (n choose 0)^2 * (n - 0) + (n choose 1)^2 * (n - 1)
inv = [0, 1]
inv_n = exp_by_sq(n, p - 2, p)  # n^(-1) mod p

for i in range(2, m + 1):
    inv_i = ( inv[p % i] * (p - p//i) ) % p  # inverse of i
    inv.append(inv_i)
    binom = (binom * (n - i + 1) % p) * inv_i % p
    ans = (ans + (binom * binom % p) * (n - i)) % p

ans = ans * inv_n % p
print(ans)
