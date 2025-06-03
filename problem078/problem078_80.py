MOD = int(1e9+7)

N = int(input())

# all posible list
Na = pow(10, N, MOD)

# number of list without 0
N0 = pow(9, N, MOD)

# number of list without both 0 and 9
N09 = pow(8, N, MOD)

M = Na - 2*N0 + N09

print(M%MOD)

