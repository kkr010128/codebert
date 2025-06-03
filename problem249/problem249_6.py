a, b, c = input().split()
x = int(a)
y = int(b)
z = int(c)
if z >= x:
    z -= x
    x = 0

else:
    x -= z
    z = 0

if z >= y:
    z -= y
    y = 0

else:
    y -= z
    z = 0

print(str(x),str(y))
