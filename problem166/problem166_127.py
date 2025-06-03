from collections import defaultdict

s = input()
d = defaultdict(int)
tmp = 0
for i in range(len(s)):
    tmp += int(s[-i - 1]) * pow(10, i, 2019)
    tmp %= 2019
    d[tmp] += 1

ans = 0
for key, value in d.items():
    if key == 0:
        ans += value * (value + 1) // 2
    else:
        ans += value * (value - 1) // 2

print(ans)
