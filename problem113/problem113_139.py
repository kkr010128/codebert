import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def calcScore(t, s, c):
    scores = [0]*26
    lasts = [0]*26
    for i in range(1, len(t)):
        scores[t[i]] += s[i][t[i]]
        dif = i - lasts[t[i]]
        scores[t[i]] -= c[t[i]] * dif * (dif-1) // 2
        lasts[t[i]] = i
    for i in range(26):
        dif = len(t) - lasts[i]
        scores[i] -= c[i] * dif * (dif-1) // 2
    return scores

def update(socre, day, t, q):
    p = t[day]
    t[day] = q
    scores[p] = 0
    scores[q] = 0
    lasts = [0]*26
    for i in range(1, len(t)):
        if t[i] == p or t[i] == q:
            scores[t[i]] += s[i][t[i]]
            dif = i - lasts[t[i]]
            scores[t[i]] -= c[t[i]] * dif * (dif-1) // 2
            lasts[t[i]] = i
    for i in [p, q]:
        dif = len(t) - lasts[i]
        scores[i] -= c[i] * dif * (dif-1) // 2
    return scores

def greedy(c, s):
    day_lim = len(s)
    socres = [0]*26
    t = [0]*day_lim
    lasts = [0]*26
    for i in range(1, day_lim):
        pls = [v for v in socres]
        mns = [v for v in socres]
        for j in range(26):
            pls[j] += s[i][j]
            mns[j] -= c[j] * (i - lasts[j])
        sum_mns = sum(mns)
        pt = sum_mns - mns[0] + pls[0]
        idx = 0
        for j in range(1, 26):
            tmp = sum_mns - mns[j] + pls[j]
            if pt < tmp:
                pt = tmp
                idx = j
        t[i] = idx
        lasts[idx] = i
        for j in range(26):
            if j == idx:
                socres[j] = pls[j]
            else:
                socres[j] = mns[j]
    return socres, t

D = int(input())
c = list(map(int, input().split()))
s = [[0]*26 for _ in range(D+1)]
for i in range(1, D+1):
    s[i] = list(map(int, input().split()))

scores, t = greedy(c, s)

for v in t[1:]:
    print(v+1)