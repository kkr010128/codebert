n = list(map(int, input().split()))
a = n[0]
b = n[1]
d = a // b
r = a % b
f = a / b
print('{} {} {:.5f}'.format(d, r, f))