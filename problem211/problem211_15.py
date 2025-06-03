n,r = input().split()
if int(n) >= 10:
    print(r)
else:
    k = (-int(r) - 100 * (10 - int(n) )) * -1
    print(k)
