N = int(input())

A = []
xy = []

for i in range(N):
    a = int(input())
    A.append(a)
    xy.append([list(map(int, input().split())) for j in range(a)])

ans = 0
p = [-1]*N

def dfs(i, p):
    global ans
    if i == N:
        ans = max(ans, sum(p))
    else:
        p_true = p.copy()
        if p_true[i] != 0:
            p_true[i] = 1
            ok = True
            for x, y in xy[i]:
                if y == p_true[x-1] or p_true[x-1] == -1:
                    p_true[x-1] = y
                else:
                    ok = False
            if ok:
                dfs(i+1, p_true)
        p_false = p.copy()
        if p_false[i] != 1:
            p_false[i] = 0
            dfs(i+1, p_false)

dfs(0, p)

print(ans)


    

