s = []
h = []
c = []
d = []
for i in range(1, 14):
    s.append('S ' + str(i))
    h.append('H ' + str(i))
    c.append('C ' + str(i))
    d.append('D ' + str(i))

n = int(input())
i = 1
while i <= n:
    a = str(input())
    if (a in s):
        s.remove(a)
    elif (a in h):
        h.remove(a)
    elif (a in c):
        c.remove(a)
    elif (a in d):
        d.remove(a)
    i += 1

if (len(s) > 0):
    print('\n'.join(s))
if (len(h) > 0):
    print('\n'.join(h))
if (len(c) > 0):
    print('\n'.join(c))
if (len(d) > 0):
    print('\n'.join(d))