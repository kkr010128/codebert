a=[list(map(int,input().split())) for _ in range(3)]
n=int(input())
b=set()
c=[[0,0,0] for _ in range(3)]
for i in range(n):
    b.add(int(input()))
for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            c[i][j]=1
for i in range(3):
    if sum(c[i])==3:
        print("Yes")
        exit()
    elif c[0][i]+c[1][i]+c[2][i]==3:
        print("Yes")
        exit()

if c[0][0]+c[1][1]+c[2][2]==3:
    print("Yes")
elif c[0][2]+c[1][1]+c[2][0]==3:
    print("Yes")
else:
    print("No")