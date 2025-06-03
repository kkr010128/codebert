n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p1 = p2 = p3 = pi = 0
for i in range(n):
    p1 += abs(a[i] - b[i])
    p2 += (abs(a[i] - b[i]))**2
    p3 += (abs(a[i] - b[i]))**3
    if pi < abs(a[i] - b[i]):
        pi = abs(a[i] - b[i])

print("%f" % (p1))
print("%f" % (p2**(1/2)))
print("%f" % (p3**(1/3)))
print("%f" % (pi))