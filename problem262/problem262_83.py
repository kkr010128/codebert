n = int(input())
tst = [[] for i in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x,y = map(int,input().split())
        tst[i].append([x,y])
ans = 0
for bit in range(1<<n):
    honest = [0]*n
    check = 1
    for i in range(n):
        if (bit>>i)&1:
            honest[-1-i] = 1
    for i in range(n):
        if not honest[i]:
            continue
        for l in tst[i]:
            if l[1]!=honest[l[0]-1]:
                check = 0
                break
    if check:
        ans = max(ans,sum(honest))
print(ans)