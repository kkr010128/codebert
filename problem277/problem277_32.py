h,w,k = map(int,input().split())
g = [list(input()) for i in range(h)]
ans = [[1]*w for i in range(h)]
count = 1
path = False
l = []
for i in range(h):
    if "#" in g[i]:
        path = True
        done = 0
        for j in range(w):
            if g[i][j] == "#":
                done += 1
                if done >= 2:
                    count += 1
            ans[i][j] = count
        count += 1
        if l:
            for j in l:
                ans[j] = ans[i]
            l = []
    else:
        if path:
            ans[i] = ans[i-1]
        else:
            l.append(i)
for i in ans:
    print(*i)
