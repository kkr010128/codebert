a,b = input().split()

a = int(a)
b = int(b)

d = a // b
r = a % b
f = a / b
f = "{0:.8f}".format(f)

fmt = "{v} {c} {n}"
s = fmt.format(v = d,c = r,n = f)
print(s)