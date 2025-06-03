from collections import defaultdict

s = input()

rests = [0]
n = 0
a = 0
m = 1
c = defaultdict(int)
c[0] += 1
for i in list(s)[::-1]:
    n = n + int(i)*m

    c[n % 2019] += 1
    m = m * 10 % 2019

for v in c.values():
    a += v * (v-1) // 2
print(a)




