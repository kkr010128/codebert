N = int(input())
A_list = list(map(int, input().split()))
MOD = 10**9 + 7

zeros = [0] * 61
ones = [0] * 61

for a in A_list:
    for i, b in enumerate([1 if (a >> j & 1) else 0 for j in range(61)]):
        if b == 1:
            ones[i] += 1
        else:
            zeros[i] += 1

res = 0
for a in A_list:
    twice = 1
    for i, b in enumerate([1 if (a >> j & 1) else 0 for j in range(61)]):
        if b == 1:
            cnt = zeros[i]
            ones[i] -= 1
        else:
            cnt = ones[i]
            zeros[i] -= 1
        res += twice * cnt
        twice *= 2
    res %= MOD
print(res)