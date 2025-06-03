n = int(raw_input())
a = 1
b = 1
for i in range(n-1):
    tmp = a
    a = b
    b += tmp
print b