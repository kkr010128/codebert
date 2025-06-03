s = input()[::-1]

cnts = [0] * 2019
cnts[0] = 1

n, d = 0, 1

for char in s:
    n = (n + int(char) * d) % 2019
    d = d * 10 % 2019
    cnts[n] += 1

ans = 0
for cnt in cnts:
    ans += cnt * (cnt - 1) // 2

print(ans)
