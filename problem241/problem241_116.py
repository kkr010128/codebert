import numpy as np
from collections import deque
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0
for i in range(len(s)):
    for j in range(len(s[0])):
        if s[i][j] == '#':
            continue
        pre = 0
        p = np.full((h, w), -1)
        p[i][j] = 0
        check = deque([((i, j), 0)])#(from,now, dist)
        while check:
            now, d = check.popleft()
            pre = max(pre, d)
            for k, l in [(1,0), (-1,0),(0,1), (0,-1)]:
                b = now[0] + k
                c = now[1] + l
                if b < 0 or c < 0 or b >= h or c >= w:
                    continue 
                elif p[b][c] == -1 and s[b][c] != '#':
                    check.append(((b, c), d + 1))
                    p[b][c] = d + 1
        ans = max(ans, pre)

print(ans)