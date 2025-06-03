a, b = map(int, input().split())
d = int(a / b)
r = a % b
f = float(a / b)
print("{0} {1} {2:.6f}".format(d, r, f))