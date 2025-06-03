n=int(input())
s=input()

ans=0
for i in range(2,n):
    if s[i-2:i+1]=='ABC':
        ans+=1
print(ans)