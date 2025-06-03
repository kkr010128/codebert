s = input()

MOD = 2019
d = [0] * MOD
d[0] = 1
r = 0
t = 1
for i in reversed(s):
    r += int(i) * t
    r %= MOD
    t *= 10
    t %= MOD
    d[r] += 1

print(sum(i * (i - 1) // 2 for i in d))