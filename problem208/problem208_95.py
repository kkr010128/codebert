n,m = map(int,input().split())
anli = [-1]*n
poss = 0
for i in range(m):
    s,c = map(int,input().split())
    if anli[s-1] == -1:
        anli[s-1] = c
    elif anli[s-1] == c:
        continue
    else:
        poss = 1
        break
if n == 1:
    if poss == 1:
        print(-1)
    else:
        if anli[0] == -1:
            print(0)
        else:
            print(anli[0])
else:
    if anli[0] == 0 or poss == 1:
        print(-1)
    else:
        if anli[0] == -1:
            anli[0] = 1
        for i in range(n):
            if anli[i] == -1:
                anli[i] = 0
            print(anli[i],end=(''))