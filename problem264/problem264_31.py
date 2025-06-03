m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())
ok = False
if d1+1 != d2:
    ok = True
if ok:
    print(1)
else:
    print(0)