h, w, k = map(int, input().split())
S = []
for i in range(h):
    s = str(input())
    S.append(s)

Ans = [[False for _ in range(w)] for _ in range(h)]

now = 1
for i in range(h):
    for j in range(w):
        if S[i][j] == '#':
            Ans[i][j] = now
            now += 1

for i in range(h):
    now = False
    for j in range(w):
        if now == False and Ans[i][j] == False:
            continue
        elif now != False and Ans[i][j] == False:
            Ans[i][j] = now
        elif Ans[i][j] != False:
            now = Ans[i][j]

for i in range(h):
    now = False
    for j in range(w-1, -1, -1):
        if now == False and Ans[i][j] == False:
            continue
        elif now != False and Ans[i][j] == False:
            Ans[i][j] = now
        elif Ans[i][j] != False:
            now = Ans[i][j]

now = False
for i in range(h):
    if now == False and Ans[i].count(False) == w:
        continue
    elif now != False and Ans[i].count(False) == w:
        Ans[i] = now
    elif Ans[i].count(False) != w:
        now = Ans[i]

now = False
for i in range(h-1, -1, -1):
    if now == False and Ans[i].count(False) == w:
        continue
    elif now != False and Ans[i].count(False) == w:
        Ans[i] = now
    elif Ans[i].count(False) != w:
        now = Ans[i]

for i in range(h):
    print(' '.join(map(str, Ans[i])))