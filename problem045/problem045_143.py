a, b = [float(i) for i in input().split()]

d = int(a / b)
r = int(a % b)
f = float(a) / float(b)

print('%s %s %.5f' %(d, r, f))