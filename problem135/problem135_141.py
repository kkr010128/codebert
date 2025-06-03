a, b = map(str, input().split())
a = int(a)
c, d = map(int, b.split('.'))
b = c * 100 + d
b *= a
print(int(("00" + str(b))[:-2]))