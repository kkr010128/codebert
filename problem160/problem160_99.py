length, Max, q = map(int,input().split())
query = [[0]*4 for _ in range(q)]
for i in range(q):
    a,b,c,d = map(int,input().split())
    query[i] = [a-1,b-1,c,d]
ans = 0
def dfs(A):
    if len(A) == length:
        global ans
        score = 0
        for i in range(q):
            a,b,c,d = query[i]
            if A[b] - A[a] == c:
                score += d
        ans = max(ans, score)
        return
    last = A[-1]
    for i in range(last,Max+1):
        A.append(i)
        dfs(A)
        A.pop()
dfs([1])
print(ans)



