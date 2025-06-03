y,x=[int(i) for i in input().split()]
s=[[int(0)for i in range(x+1)]for j in range(y+1)]
for i in range(y):
    k=input().split()
    for j in range(x):
        s[i][j]=int(k[j])
for i in range(y):
    for j in range(x):
        s[i][x]=s[i][x]+s[i][j]
        s[y][j]=s[y][j]+s[i][j]
for i in range(y):
    s[y][x]=s[y][x]+s[i][x]
for i in range(y+1):
    for j in range(x):
        print(s[i][j],"",end="")
    print(s[i][x])