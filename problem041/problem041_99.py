w, h, x, y, r = map(int, input().split())
print("Yes" if r <= x <= w - r and r <= y <= h -r else "No")