def dfs(seq):
    ans = 0

    if len(seq) == n:
        score = 0
        for a, b, c, d in req:
            if seq[b-1] - seq[a-1] == c:
                score += d
        return score
    else:
        for i in range(seq[-1], m+1):
            next_seq = seq + (i,)
            score = dfs(next_seq)
            ans = max(ans, score)
    return ans

n, m, q = list(map(int, input().split()))
req = [list(map(int, input().split())) for _ in range(q)]

print(dfs((1,)))
