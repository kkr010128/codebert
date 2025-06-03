n,r = map(int,input().split())

if n > 10:
    print(r)
else:
    a = r + (100 * (10-n))
    print(a)

