N = int(input())

#U:0~9の整数でN桁の数列 = 10**N
#A:0を含まないN桁の数列 = 9**N
#B:9を含まないN桁の数列 = 9**N

#ans = |U-(A∪B)| = |U|-|A|-|B|+|A∩B|

MOD = 10**9 + 7
ans = pow(10, N, MOD) - pow(9, N, MOD) - pow(9, N, MOD) + pow(8, N, MOD)
ans %= MOD

print(ans)