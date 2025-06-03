s = input()
s = s[::-1]
m = [0] * 2019
m[0] = 1
a = 0
d = 1
ans = 0
for si in s:
    a = (a + int(si) * d) % 2019
    d = (d * 10) % 2019
    ans += m[a]
    m[a] += 1
print(ans)
