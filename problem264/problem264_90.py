m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())
if d1 == 31:
    print("1")
elif d1 == 30 and d2 == 1:
    print("1")
elif d1 == 28 and m1 == 2:
    print("1")
else:
    print("0")