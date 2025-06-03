import sys
input = sys.stdin.readline
MOD = pow(10, 9) + 7


n = int(input())
a = list(map(int, input().split()))

m = max(a)

num = [0] * 61

for x in a:
    for j in range(61):
        if (x >> j) & 1:
            num[j] += 1

s = 0

#print(num)

for i in range(61):
    s += (n - num[i]) * num[i] * pow(2, i, MOD) % MOD

print(s % MOD)