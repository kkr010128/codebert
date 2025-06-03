W, H, x, y, r = map(int, input().split())

delta = [[r, 0], [-r, 0], [0, r], [0, -r]]

for dx, dy in delta:
    if 0 <= x + dx <= W and 0 <= y + dy <= H:
        pass
    else:
        print('No')
        exit(0)

print('Yes')
