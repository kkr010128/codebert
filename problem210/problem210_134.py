import sys
import bisect

N = int(sys.stdin.readline().rstrip())
S = list(sys.stdin.readline().rstrip())
Q = int(sys.stdin.readline().rstrip())

idx = {chr(ord("a") + i): [] for i in range(26)}

for i, s in enumerate(S):
    idx[s].append(i + 1)

for _ in range(Q):
    t, i, c = sys.stdin.readline().rstrip().split()
    i = int(i)
    if t == "1":
        if S[i - 1] != c:
            idx[S[i - 1]].remove(i)
            bisect.insort(idx[c], i)
            S[i - 1] = c
    else:
        c = int(c)
        ans = 0
        for a, id in idx.items():
            x = bisect.bisect_left(id, i)
            y = bisect.bisect_right(id, c)
            if y - x:
                ans += 1
        print(ans)