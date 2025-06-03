rc=list(map(int,input().split()))
sheet=[list(map(int,input().split()))+[0] for i in range(rc[0])]
sheet.append([0 for i in range(rc[1]+1)])
for s in sheet:
    s[-1]=sum(s[0:-1])
for i in range(rc[1]+1):
    r=sum([n[i] for n in sheet[0:-1]])
    sheet[-1][i]=r
for sh in sheet:
    print(*sh)