import math
N = int(input())

MOD_VALUE = math.pow(10, 9) + 7

def pow_mod(value, pow):
    ret = 1
    for _ in range(pow):
        ret = ret * value % MOD_VALUE
    return ret

result = pow_mod(10, N) - pow_mod(9, N) * 2 + pow_mod(8, N)

print(int(result % MOD_VALUE))
