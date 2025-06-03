import copy
from collections import Counter

h, w, K = map(int, input().split())



c = [[False for _ in range(w)] for _ in range(h)]
for i in range(h):
    s = input()
    for j in range(len(s)):
        if s[j] == '#':
            c[i][j] = True


cnt = 0
for i in range(2**h):
    tmp = copy.deepcopy(c)
    for j in range(h):
        if((i >> j) & 1):
            tmp[j] = [False for _ in range(w)] 

    for k in range(2**w):
        tmp2 = copy.deepcopy(tmp)
        for m in range(w):
            if((k >> m) & 1):
                for a in range(h):
                    tmp2[a][m] = False
            
        if sum(tmp2, []).count(True) == K:
            cnt += 1

print(cnt)
