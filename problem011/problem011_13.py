a,b=[int(x) for x in input().split()]

x = max(a,b)
y = min(a,b)
res = y

while x%y>0:
    res = x%y
    x = y
    y = res

print(res)