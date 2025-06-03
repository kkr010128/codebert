n, m, q = map(int, input().split())
query = [tuple(map(int, input().split())) for _ in range(q)]

def score(A):
    ret = 0
    for a, b, c, d in query:
        if A[b-1] - A[a-1] == c:
            ret += d
    return ret

def dfs(pre, _min):
    if len(pre) == n:
        return score(pre)
    ret = 0
    for i in range(_min, m+1):
        new = pre + [i]
        ret = max(ret, dfs(new, i))
    return ret

print(dfs([], 1))