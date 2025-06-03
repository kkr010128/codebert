r=input().split()
N=int(r[0])
D=int(r[1])
ans=0
d=[input().split() for i in range(N)]
for i in range(N):
    if int(d[i][1])**2+int(d[i][0])**2<=D**2:
        ans+=1
print(ans)