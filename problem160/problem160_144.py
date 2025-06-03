  
def dfs(A):
    if len(A) == n+1:
        global ans
        total = 0
        for i in range(q):
            if A[b[i]]-A[a[i]] == c[i]:
                total += d[i]
        if total > ans:
            ans = total
        return
    num = A[-1]
    while num <= m:
        dfs(A[:]+[num])
        num += 1
    
                

if __name__ == "__main__":
    n, m, q = map(int, input().split())
    a, b, c, d = [None]*q, [None]*q, [None]*q, [None]*q
    for i in range(q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    ans = 0
    dfs([1])
    print(ans)