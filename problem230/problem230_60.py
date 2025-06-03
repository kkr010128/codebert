
from bisect import bisect_right

N, D, A = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

X.sort()
place = []
hps = []
for x, h in X:
    place.append(x)
    hps.append(h)

buf = [0] * (N + 2)
ans = 0
for i in range(N):
    # Update
    buf[i + 1] += buf[i]

    # Calc count
    tmp = -(-max(0, hps[i] - buf[i + 1] * A) // A)
    ans += tmp

    # Calc range
    j = bisect_right(place, place[i] + D * 2)
    buf[i + 1] += tmp
    buf[min(j + 1, N + 1)] -= tmp

print(ans)
