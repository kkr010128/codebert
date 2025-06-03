n, k = map(int, input().split())
p = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))

ans = - 10 ** 18
for i in range(1, n+1):
    base = i
    nxt = p[i]
    cnt = 0
    score = 0
    while True:
        cnt += 1
        if cnt > k:
            break
        score += c[nxt]
        ans = max(ans, score)
        #print("i = ", i, "ans = ", ans, "score = ", score)
        if nxt == base:
            break
        nxt = p[nxt]
    if cnt >= k:
        continue
    extra = k - cnt
    score_tmp = score
    nxt = p[nxt]
    nxt_tmp = nxt
    for j in range(min(extra, cnt)):
        score += c[nxt]
        ans = max(ans, score)
        #print("ans = ", ans, "score = ", score, "nxt = ", nxt, "c[nxt] = ", c[nxt])
        nxt = p[nxt]
    #print("score = ", score, "ans = ", ans)
    score = score_tmp
    nxt = nxt_tmp
    a = extra // cnt
    if extra % cnt == 0:
        a -= 1
    score += score * max(a, 0)
    ans = max(ans, score)
    for j in range(extra - a * cnt):
        score += c[nxt]
        ans = max(ans, score)
        #print("ans = ", ans, "score = ", score, "nxt = ", nxt, "c[nxt] = ", c[nxt])
        nxt = p[nxt]

print(ans)