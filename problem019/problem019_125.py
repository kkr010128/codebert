n, time=map(int,raw_input().split())
p = []
t = []
for _ in xrange(n):
    a = raw_input().split()
    p.append(a[0])
    t.append(int(a[1]))
alltime = 0
while True:
    if len(p)==0:
        break
    if t[0]<=time:
        alltime+=t[0]
        print p.pop(0),
        t.pop(0)
        print alltime
    else:
        t.append(t[0])
        t.pop(0)
        t[-1]-=time
        alltime += time
        p.append(p[0])
        p.pop(0)