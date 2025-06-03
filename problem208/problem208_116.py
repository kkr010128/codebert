N, M = map(int, input().split())

S = []
C = []
for m in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

tmp_ans = []
for n in range(10**N):
    n = str(n)

    if len(n)<N:
        continue

    flag = True
    for s, c in zip(S,C):
        if int(n[s-1]) != c:
            flag = False
            break

    if flag:
        tmp_ans.append(n)

if len(tmp_ans)>0:
    print(min(tmp_ans))
else:
    print(-1)
