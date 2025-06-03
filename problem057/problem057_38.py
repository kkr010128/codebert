m = []
f = []
r = []
while(1):
    a,b,c = map(int,raw_input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        m.append(a)
        f.append(b)
        r.append(c)

for i in range(len(m)):
    if m[i] == -1 or f[i] == -1:
        print "F"
    elif m[i] + f[i] >= 80:
        print "A"
    elif m[i] + f[i] >= 65:
        print "B"
    elif m[i] + f[i] >= 50 or r[i] >= 50:
        print "C"
    elif m[i] + f[i] >= 30:
        print "D"
    else:
        print "F"
