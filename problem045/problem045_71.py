L = raw_input().split()
a = int(L[0])
b = int(L[1])
d = int(0)
r = int(0)
f = float(0)

d = a / b
r = a % b
f = float(a) / float(b)

print "{0} {1} {2:f}".format(d,r,f)