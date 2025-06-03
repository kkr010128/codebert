n, m = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(m)]

ans = [-1]*n
flag = False

for s, c in X:
    if ans[s-1] >= 0 and ans[s-1] != c:
        flag = True
    if n > 1 and s == 1 and c == 0:
        flag = True
    else:
        ans[s-1] = c

if flag:
    print(-1)
    exit(0)

for i in range(n):
    if ans[i] == -1:
        if n > 1 and i == 0:
            ans[i] = 1
        else:
            ans[i] = 0

print(*ans, sep="")