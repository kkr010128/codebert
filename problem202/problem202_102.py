n,b,r = map(int, input().split())
t = n % (b+r)
q = n // (b+r) * b
if t > b:
    t = b

print(q+t)
