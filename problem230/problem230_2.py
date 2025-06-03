import sys
from bisect import bisect_right
from operator import itemgetter

read = sys.stdin.read

N, D, A, *XH = map(int, read().split())
XH = sorted(zip(*[iter(XH)] * 2), key=itemgetter(0))
D *= 2
X = [i for i, _ in XH]

damages = [0] * (N + 2)
answer = 0

for i, (x, h) in enumerate(XH, 1):
    damages[i] += damages[i - 1]
    if damages[i] >= h:
        continue

    h -= damages[i]
    cnt = (h + A - 1) // A
    answer += cnt
    damage = A * cnt
    damages[i] += damage
    damages[bisect_right(X, x + D) + 1] -= damage

print(answer)
