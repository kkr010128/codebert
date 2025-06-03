x = raw_input()
a, b = x.split()
a = int(a)
b = int(b)

#d
d = a / b
d = d

#r
r = a % b

#f
f = float(a) / float(b)

print("%d %d %.5f" %(d, r, f))