import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def keyence20_a():
    H, W, N = map(int, readlines())
    lg = max(H, W)
    ans = (N + lg - 1) // lg
    print(ans)

keyence20_a()