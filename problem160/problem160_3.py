n, m, q = map(int, input().split())
a = [0] * q
b = [0] * q
c = [0] * q
d = [0] * q
for i in range(q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

score = []

# 数列Aの全探索

import copy
def dfs(A):
    if len(A) == n+1:
        # score計算
        tmp = 0
        #print(A)
        for i in range(q):
            if A[b[i]] - A[a[i]] == c[i]:
                 tmp += d[i]
        score.append(tmp)
        return
    else:
        tmp = A[-1]
        arr = copy.copy(A)
        arr.append(tmp)
        while(arr[-1] <= m):
            dfs(arr)
            arr[-1] += 1  
dfs([1])

print(max(score))
