N = input()
a = []
for i in range(N):
    a.append(map(int, raw_input().split()))

for j in range(N):

    x = a[j][0] ** 2
    y = a[j][1] ** 2
    z = a[j][2] ** 2

    if x == y + z:
        print "YES"
    elif y == x + z:
        print "YES"
    elif z == x + y:
        print "YES"
    else:
        print "NO"