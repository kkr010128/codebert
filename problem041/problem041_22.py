from sys import stdin

W, H, x, y, r = (int(n) for n in stdin.readline().rstrip().split())

answer = "Yes" if r <= x <= W - r and r <= y <= H - r else "No"

print(answer)

