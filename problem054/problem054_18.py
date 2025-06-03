s = [0] * 13
h = [0] * 13
c = [0] * 13
d = [0] * 13

num = int(input())
for i in range(num):
    m, n = input().split()
    x = int(n) - 1
    if m == "S":
        s[x] = 1
    elif m == "H":
        h[x] = 1
    elif m == "C":
        c[x] = 1
    elif m == "D":
        d[x] = 1
    else:
        break

for i in range(13):
    if s[i] == 0:
        print("S %d" % (i+1))

for i in range(13):
    if h[i] == 0:
        print("H %d" % (i+1))

for i in range(13):
    if c[i] == 0:
        print("C %d" % (i+1))

for i in range(13):
    if d[i] == 0:
        print("D %d" % (i+1))




