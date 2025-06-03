N = int(raw_input())

for i in range(N):
    a = range(3)
    a[0],a[1],a[2] = map(int, raw_input().split())
    a.sort()
    if a[0]**2 + a[1]**2 == a[2]**2:
        print "YES"
    else:
        print "NO"