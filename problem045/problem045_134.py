a, b = input().split()
a = int(a)
b = int(b)

d = int(a/b)
r = a%b
f = a/b

print(str(d) + " " + str(r) + " " + "%.8f" % (f))