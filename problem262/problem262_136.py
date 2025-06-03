n = int(input())
XY = [[] for _ in range(n)]
ans = 0

for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        XY[i].append((x-1, y))

for i in range(2**n):
    correct = [False]*n
    tmp_cnt = 0
    flag = True

    for j in range(n):
        if i&(1<<j):
            correct[j] = True
            tmp_cnt += 1

    for j in range(n):
        if correct[j]:
            for x, y in XY[j]:
                if (y==0 and correct[x]) or (y==1 and not correct[x]):
                    flag = False
    if flag:
        ans = max(tmp_cnt, ans)

print(ans)