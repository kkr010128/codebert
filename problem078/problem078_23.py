mod = 10 ** 9 + 7

N = int(input())

result = 0

ten = pow(10, N, mod)
nine = pow(9, N, mod)
eight = pow(8, N, mod)

result = (ten - 2 * nine + eight) % mod

print(result)