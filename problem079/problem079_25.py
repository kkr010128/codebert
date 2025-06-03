mod = 10 ** 9 + 7
s = int(input())
dp = []
for i in range(s):
    v = 0
    if i >= 2:
        v += 1
        v += sum(dp[:i - 2])
    v %= mod
    dp.append(v)
print(dp[-1])
