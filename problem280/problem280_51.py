N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
ans = []
import numpy as np
for i in range(len(A)-1):
    for k in range(i+1,len(A)):
        ans.append(np.sqrt(((A[i][0]-A[k][0])**2)+(A[i][1]-A[k][1])**2))
print(sum(ans)*2/N)