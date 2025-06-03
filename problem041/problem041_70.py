W, H, x, y, r = list(map(int, input().split()))

x_right = x + r
x_left = x - r
y_up = y + r
y_down = y - r

if x_right <= W and x_left >= 0 and y_up <= H and y_down >= 0:
    print("Yes")
else:
    print("No")

