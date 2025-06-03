a,b = input().split()

x = int(a) * b
y = int(b) * a
l = []
l.append(x)
l.append(y)
l = sorted(l)

print(min(l))