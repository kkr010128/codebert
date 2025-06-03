N=int(input())

L=[]
# xでソート
#でソート
#min, max


for i in range(N):
    x,y=map(int, input().split())
    L.append([x+y,x-y])
    

L=sorted(L)
ans=abs(L[0][0]-L[-1][0])
L=sorted(L, key=lambda x: x[1])
ans=max(ans, abs(L[0][1]-L[-1][1]))

print(ans)