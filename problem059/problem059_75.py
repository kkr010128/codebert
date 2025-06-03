rc=list(map(int,input().split()))
a=[[0 for x in range(rc[1]+1)]for x in range(rc[0]+1)]
for x in range(rc[0]):
    code=list(map(int,input().split()))
    result=0
    for y in range(rc[1]):
        a[x][y]=code[y]
        result+=code[y]
    a[x][rc[1]]=result

for y in range(rc[1]+1):
    result=0
    for x in range(rc[0]):
        result+=a[x][y]
    a[rc[0]][y]=result

for x in range(rc[0]+1):
    string=""
    for y in range(rc[1]+1):
        string+=str(a[x][y])
        if (y!=rc[1]):
            string+=" "
    print(string)