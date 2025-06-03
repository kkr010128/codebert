a,b = map(str, input().split())
a2 = a*int(b)
b2 = b*int(a)
print(a2) if a2 < b2 else print(b2)
