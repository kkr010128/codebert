n, m = map(int, input().split())
ans = [-1 for _ in range(n)]
for _ in range(m):
    s, c = map(int, input().split())
    if ans[s - 1] in [c, -1]:
        ans[s - 1] = c
    else:
        print(-1)
        exit()
if ans[0] == 0:
    if n == 1:
        print(0)
    else:
        print(-1)
    exit()
if ans[0] == -1:
    if n == 1:
        print(0)
        exit()
    ans[0] = 1
ret = str(ans[0])
for i in range(1, n):
    if ans[i] == -1:
        ans[i] = 0
    ret += str(ans[i])
print(int(ret))
