x, y = map(int, input().split())
if y % 2 != 0:
    print("No")
else:
    if 2 * x <= y <= 4 * x:
        print("Yes")
    else:
        print("No")