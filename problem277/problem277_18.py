h , w , k = map(int,input().split())
ans = []
cake = []
cou = 0
for i in range(h):
    cake.append(list(input()))
fla = 0
for i in range(h):
    if cake[i].count("#") == 0:
        if i == 0:
            fla = 1
            ans.append([]) 
        elif i != 0:
            if fla == 0:
                ans.append(ans[i-1])
            elif fla == 1:
                ans.append([])
    else:
        cou += 1
        p = 0
        kar = []
        for j in range(w):
            if cake[i][j] == "#":
                if p == 0:
                    p = 1
                elif p != 0:
                    cou += 1
            kar.append(cou)
        ans.append(kar)
        if fla == 1:
            fla = 0
            tyu = 0
            while True:
                if ans[tyu] == []:
                    ans[tyu] = kar
                else:
                   break
                tyu += 1
for i in range(h):
    print(*ans[i])