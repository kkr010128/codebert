s = input()
s = s[::-1]
n = len(s)
m = [0] * 2019
m[0] = 1
a = 0
d = 1
for i in range(n):
    a = (a + int(s[i]) * d) % 2019
    d = (d * 10) % 2019
    m[a] += 1
print(sum([int(x * (x - 1) / 2) for x in m if x > 1]))
