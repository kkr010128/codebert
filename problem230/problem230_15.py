import sys
input = sys.stdin.readline
from collections import deque
import math


n, d, a = map(int, input().split())

XH = []
for _ in range(n):
    x, h = map(int, input().split())
    XH.append((x, h))
XH.sort()

answer = 0
damage = 0
QUEUE = deque()
for x, h in XH:
    if QUEUE:
        while x > QUEUE[0][0]:
            damage -= QUEUE[0][1]
            QUEUE.popleft()
            if not QUEUE:
                break
    h -= damage
    if h <= 0:
        continue
    bomb = math.ceil(h / a)
    QUEUE.append((x + 2 * d, a * bomb))
    damage += a * bomb
    answer += bomb

print(answer)
