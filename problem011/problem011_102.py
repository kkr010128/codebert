a,b=[int(i) for i in input().split(" ")]

while b!=0:
    t = min(a,b)
    b = max(a,b) % min(a,b)
    a = t
print(a)