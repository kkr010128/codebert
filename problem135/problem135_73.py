a, b = input().split()
a = int(a)
b = int(b.replace(".",""))

c = a * b
ans = c//100
print(ans)
