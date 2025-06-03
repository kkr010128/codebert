a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
A = []
w = a * c
x = a * d
y = b * c
z = b * d
A.append(w)
A.append(x)
A.append(y)
A.append(z)
B = max(A)
print(B)