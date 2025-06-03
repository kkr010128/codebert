
N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]

cand = [-1] * N
flag = False
for s, c in X:
    s -= 1
    if cand[s] == -1:
        cand[s] = c
    elif cand[s] != c:
        flag = True

if flag or (N > 1 and cand[0] == 0):
    print(-1)
else:
    ans = 0
    for i in range(N):
        if cand[i] == -1:
            if i == 0 and N > 1:
                cand[i] = 1
            else:
                cand[i] = 0
        ans += cand[i] * 10 ** (N - i - 1)
    print(ans)
