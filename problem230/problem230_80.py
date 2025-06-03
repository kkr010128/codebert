import sys
from collections import deque
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, D, A = map(int, input().split())
XH = list(tuple(map(int, input().split())) for _ in range(N))
XH.sort()

ans = 0
memo = deque()
cnt = 0
for x, h in XH:
    while memo and memo[0][0] < x:
        _, i = memo.popleft()
        cnt -= i
    h -= cnt * A
    h = max(h, 0)
    bomb = (h + A - 1) // A
    ans += bomb
    cnt += bomb
    memo.append((x + 2 * D, bomb))

print(ans)