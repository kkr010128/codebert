n, a, b = [int(i) for i in input().split()]
a,b=max(a,b),min(a,b)

if (a - b) % 2 == 0:
    print((a - b) // 2)
else:
    c = b + (a -1- b) // 2
    d = n - a + 1 + (n - (n - a + 1) - b) // 2
    print(min(c,d))
