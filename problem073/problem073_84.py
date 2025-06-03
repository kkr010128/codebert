N=int(input())
ans=0
for i in range(1,N):
    if N%i!=0:
        for j in range(1,N//i+1):
            ans+=1
    else:
        for j in range(1,N//i):
            ans+=1
print(ans)