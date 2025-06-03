a, b, n = map(int, input().split())

c = int(a*n/b) - a*int(n/b)

if n < b:
    print(c)
else:
    c = int(a*(b-1)/b) - a*int((b-1)/b)
    print(c)