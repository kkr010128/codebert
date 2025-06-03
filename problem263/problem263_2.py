N = int(input())
A = tuple(map(int, input().split(' ')))
MOD = 10 ** 9 + 7

zeros = [0] * 60
ones = [0] * 60

for a in A:
    for i, bit in enumerate(reversed(format(a, '060b'))):
        if bit == '0':
            zeros[i] += 1
        else:
            ones[i] += 1

base = 1
ans = 0

for i in range(len(zeros)):
    ans += zeros[i] * ones[i] * base
    ans %= MOD
    base *= 2
    base %= MOD

print(ans)
