s = list(range(1,14))
h = list(range(1,14))
c = list(range(1,14))
d = list(range(1,14))

n = int(input())
while n > 0:
    x = input().split(' ')
    x[1] = int(x[1])
    if x[0] == 'S':
        s[x[1]-1] = 0
    elif x[0] == 'H':
        h[x[1]-1] = 0
    elif x[0] == 'C':
        c[x[1]-1] = 0
    elif x[0] == 'D':
        d[x[1]-1] = 0
    n -= 1

for t in s:
    if t != 0: print("S %d" % t)
for t in h:
    if t != 0: print("H %d" % t)
for t in c:
    if t != 0: print("C %d" % t)
for t in d:
    if t != 0: print("D %d" % t)