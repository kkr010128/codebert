n, m = map(int,input().split())
sc = [list(map(int,input().split())) for i in range(m)]

flg = True
for ci in range(0, 10**n):
    cis = str(ci)
    if len(cis) != n:
        continue
    for j in range(m):
        s, c = sc[j][0]-1, sc[j][1]
        if int(cis[s]) != sc[j][1]:
            flg = False
            break
            
        if j == m-1:
            flg = True
    if flg == True:
        break
print(ci) if flg else print(-1)        