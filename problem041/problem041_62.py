import sys
(W, H, x, y, r) = [int(i) for i in sys.stdin.readline().split()]
if r <= x <= W - r and r <= y <= H - r:
    print("Yes")
else:
    print("No")