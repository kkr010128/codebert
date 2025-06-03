a,b = (int(x) for x in input().split())
b *= 2
p = a - b
if p < 0:
    print(0)
else:
    print(abs(p))