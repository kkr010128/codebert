n, a, b = map(int, input().split())
q = n // (a + b)
mod = n % (a + b)
if mod > a:
    remain = a
else:
    remain = mod
    
print(q * a + remain)