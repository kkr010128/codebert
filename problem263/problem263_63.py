import math
N = int(input())
A = list(map(int, input().split()))
bit = [0] * 60
MOD = 10 ** 9 + 7
for a in A:
    i = 0
    waru = 1
    while a > 0:
        if a % (waru * 2) != 0:
            a -= waru
            bit[i] += 1
        waru *= 2
        i += 1
answer = 0
for i, b in enumerate(bit):
    answer += (2 ** i) * (b * (N-b))
print(answer % MOD)