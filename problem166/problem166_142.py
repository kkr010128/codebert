from collections import Counter
s = input()
MOD = 2019
ts = [0]
cur = 0
for i, j in enumerate(s[::-1], 1):
    cur = (cur + pow(10, i, MOD) * int(j)) % MOD
    ts.append(cur)
ct = Counter(ts)
res = 0
for k, v in ct.items():
    if v > 1:
        res += v * (v-1) // 2
print(res)