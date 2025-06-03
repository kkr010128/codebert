a,b = [float(i) for i in input().split()]
d = int(a/b)
r = int(a) % int(b)
f = a/b
f = "{:.9f}".format(f)

print(d,r,f)
