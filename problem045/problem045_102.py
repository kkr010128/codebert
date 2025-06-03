#encoding:utf-8

ab = raw_input().split()

a = int(ab[0])
b = int(ab[1])

d = a / b
r = a % b
f = round(float(a) / float(b), 5)

print d, r, f