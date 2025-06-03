x=0
b=[[0 for col in range(250)] for row in range(10)]
a="first"
while True:
    a=list(input())
    if a[0]=="-":
        break
    m=int(input())
    h=0
    ans=[0]*250
    for i in range(m):
        h=int(input())
        for j in range(h,len(a)):
            ans[j-h]=a[j]
        for k in range(h):
            ans[len(a)-h+k]=a[k]
        for l in range(len(a)):
            a[l]=ans[l]
    for y in range(len(a)):
        b[x][y]=a[y]
    x+=1


for i in range(x):
#        for j in range(len(b[x+1])):
    for j in range(200):
        if b[i][j]==0:
            break
        print(b[i][j],end="")
    print()

