import sys

S = input()[::-1]

c = [0] * 2019
c[0] = 1

num = 0
d = 1

for a in S:
    num += int(a) * d
    num %= 2019
    d *= 10
    d %= 2019
    c[num] += 1

a = 0
for i in c:
    a += i * (i - 1) // 2

print(a)

