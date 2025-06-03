r,c=map(int,input().split())
table=list()
for i in range(r):
    table.append(list(map(int,input().split())))
for i in range(r):
    for j in range(c):
        print(table[i][j],"",end="")
    print(sum(table[i]),sep="")
bottom=list()
for i in range(c):
    tmp=0
    for j in range(r):
        tmp+=table[j][i]
    bottom.append(tmp)
for i in bottom:
    print(i,"",end="")
print(sum(bottom))