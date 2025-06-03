N=int(input())
ans=0
for i in range(1,int(N**(1/2))+1):
    a=(N-1)//i
    ans+=(a-i)*2+1
if int(N**(1/2))**2==N:
    ans+=1
print(ans)