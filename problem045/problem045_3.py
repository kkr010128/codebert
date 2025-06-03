a = input().split()

d = int(a[0]) // int(a[1])
r = int(a[0]) % int(a[1])
f = float(a[0]) / float(a[1])

print('{0} {1} {2:.5f}'.format(d,r,f))
