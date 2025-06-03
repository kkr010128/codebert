n=int(input())
cnt=0
ans=0
while(n>=1):
    ans+=2**cnt
    n//=2
    cnt+=1
print(ans)