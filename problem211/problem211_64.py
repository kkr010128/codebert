n,r = list(map(int,input().split()))
inner = 0
if n >= 10:
    inner = r
else:
    inner = r + 100 * (10 - n)
print(inner)