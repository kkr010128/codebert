n= int(input())
table=[[[0]*10 for i in range(0,3)]for j in range(0,4)]
for k in range(n):
    b,f,r,v = map(int,input().split())
    table[b-1][f-1][r-1] +=v
x=0
for i in range(4):
    if x !=0:
        print("#"*20)
    x =x+1
    for a in range(3):
        for b in range(10):
            print(" %d"%(table[i][a][b]),end="")
        print()
