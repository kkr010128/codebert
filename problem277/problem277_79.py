h, w, k = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())
cnt = 1
rflg = False
rcnt = 1
for r in s:
    if r.count('#')>0:
        if rflg:
            cnt += 1
            rcnt = 1
        rflg = True
    elif rflg:
        print(*ans)
        continue
    else:
        rcnt += 1
        continue
    cflg = False
    ans = []
    for e in r:
        if e=='#':
            if cflg:
                cnt += 1
            cflg = True
        ans.append(cnt)
    for _ in range(rcnt):
        print(*ans)