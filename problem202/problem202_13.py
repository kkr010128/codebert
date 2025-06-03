n,a,b = map(int, input().split())
blue = a*(n//(a+b))
if n%(a+b) <= a:
    blue += n%(a+b)
else:
    blue += a
print(blue)