N=int(input())
xp=yp=0
xn=yn=10**9
zs=[0]*N
ws=[0]*N
for i in range(N):
    xi,yi=map(int,input().split())
    zs[i]=xi+yi
    ws[i]=xi-yi
zs.sort()
ws.sort()
ans=max(zs[-1]-zs[0],ws[-1]-ws[0])
print(ans)