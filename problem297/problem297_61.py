n = int(input())

b = range(1, n)

a = b[::2]
print(1 - (len(a) / n))
