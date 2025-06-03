h, w, k = map(int, input().split())
s = [input() for _ in range(h)]

ans = [[0 for _ in range(w)] for _ in range(h)]

num = 0
f = False
for i, j in enumerate(s):
    tmp = j.find("#")
    if tmp == -1:
        if f:
            ans[i] = ans[i - 1]
        continue
    else:
        num += 1
        for k in range(tmp + 1):
            ans[i][k] = num
        for l in range(tmp + 1, w):
            if j[l] == ".":
                ans[i][l] = num
            else:
                num += 1
            ans[i][l] = num
        if f == False:
            f = True
            for x in range(i):
                ans[x] = ans[i]

for i in ans:
    print(*i)