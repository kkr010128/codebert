W, H, x, y ,r = [int(i) for i in input().split()]

if x <= 0 or y <= 0:
    print("No")
elif W - x >= r and H - y >= r:
    print("Yes")
else:
    print("No")