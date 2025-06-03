h, w, k = map(int, input().split())
s = [input() for _ in range(h)]
ans = []
vacant = 0
cnt = 0
for x in range(h):
    if s[x] == '.' * w:
        vacant += 1
        continue
    else:
        cnt += 1
        tmp = []
        yet = False
        for y in range(w):
            if s[x][y] == '#':
                if not yet:
                    yet = True
                else:
                    cnt += 1
            tmp.append(cnt)
        for _ in range(vacant + 1):
            ans.append(tmp)
        vacant = 0
for _ in range(vacant):
    ans.append(ans[-1])
for a in ans:
    print(*a, sep=" ")