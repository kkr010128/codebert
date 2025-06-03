n, m, q = list(map(int, input().split()))
a=[0]*q
b=[0]*q
c=[0]*q
d=[0]*q
for i in range(q):
    a[i],b[i],c[i],d[i] = map(int, input().split())
    a[i] -=1
    b[i] -=1

def score(A):
    score =0
    for ai, bi, ci, di in zip(a,b,c,d):
        if A[bi] - A[ai] == ci:
            score += di
    return score

def dfs(A):
    if len(A)==n:
        #print(A)
        return score(A)
    res = 0
    if len(A) > 0:
        last_term = A[-1]
    else:
        last_term = 1
    for i in range(last_term, m+1):
        A.append(i)
        res = max(res, dfs(A))
        A.pop()
    
    return res

print(dfs([]))