N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
ans = []
import numpy as np
import itertools
for zyun in itertools.permutations(range(N)):
    cnt = 0
    for k in range(len(zyun)-1):
        cnt += np.sqrt((A[zyun[k+1]][0]-A[zyun[k]][0])**2+(A[zyun[k+1]][1]-A[zyun[k]][1])**2 )
    ans.append(cnt)
print(sum(ans) / len(ans))