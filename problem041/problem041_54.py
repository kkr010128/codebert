W, H, x, y, r = map(int, input().split())

flg = False
for X in [x - r, x + r]:
    for Y in [y - r, y + r]:
        if not 0 <= X <= W:
            flg = True
        if not 0 <= Y <= H:
            flg = True

print(["Yes", "No"][flg])
