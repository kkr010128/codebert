x, y = map(int, input().split())
if y/2 != int(y/2):
    print("No")
else:
    p = 2*x - y/2
    q = y/2 - x
    if p >= 0:
        if q >= 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")