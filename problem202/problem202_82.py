n, a, b = map(int,input().split())

c = n % (a + b)
d = n // (a + b)

if c <= a:
    ans = d * a + c
else:
    ans = d * a + a

print(ans)