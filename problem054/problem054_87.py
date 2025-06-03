n = input()
s = range(1,14)
h = range(1,14)
c = range(1,14)
d = range(1,14)


for i in range(n):
    a = raw_input().split()
    num = int(a[1])
    if a[0] == "S":
        s.remove(num)
    elif a[0] == "H":
        h.remove(num)
    elif a[0] == "C":
        c.remove(num)
    elif a[0] == "D":
        d.remove(num)


for i in range(len(s)):
    print "S",s[i]
for i in range(len(h)):
    print "H",h[i]
for i in range(len(c)):
    print "C",c[i]
for i in range(len(d)):
    print "D",d[i]