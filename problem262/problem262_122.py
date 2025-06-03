N = int(input())
say = {}
for i in range(N):
    say[i] = []
    A = int(input())
    for j in range(A):
        x, y = map(int, input().split())
        x -= 1
        say[i].append((x, y))
ans = 0
for i in range(1 << N):
    ok = True
    Honecount = 0
    for j in range(N):
        if((i >> j) & 1 == 0):
            continue
        Honecount += 1
        for k in say[j]:
            if ((i >> k[0]) & 1) != k[1]:
                ok = False
                break
        if ok == False:
            break
    if ok == True:
        ans = max(ans, Honecount)

print(ans)
