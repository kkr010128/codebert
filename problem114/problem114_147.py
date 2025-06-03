d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]
t = [int(input()) - 1 for _ in range(d)]

def scoring(d, c, s, t):
    v = []
    memo = [0 for _ in range(26)]
    for i in range(d):
        if i == 0:
            score = 0
        else:
            score = v[-1]
        score += s[i][t[i]]
        memo[t[i]] = i + 1
        for j in range(26):
            score -= c[j] * (i+1 - memo[j])

        v.append(score)

    return v

v = scoring(d, c, s, t)
print(*v, sep='\n')