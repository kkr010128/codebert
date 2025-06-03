a,b,c,d=input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

z1 = a*c
z2 = a*d
z3 = b*c
z4 = b*d

l = [z1, z2, z3, z4]
max_value = max(l)
print(max_value)