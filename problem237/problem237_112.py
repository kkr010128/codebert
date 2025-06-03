N=int(input())
XL=[list(map(int,input().split())) for i in range(N)]

R=[]
for i in range(N):
    a=max(0,XL[i][0]-XL[i][1])
    b=XL[i][1]+XL[i][0]
    R.append([b,a])
R.sort()

ans=0
con_l=0
for i in range(N):
    if con_l <= R[i][1]:
        ans += 1
        con_l = R[i][0]
print(ans)