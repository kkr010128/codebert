n=int(input())
s,t=input().split()
ans=s[0]+t[0]
for i in range(1,n):
    ans=ans+s[i]+t[i]
print(ans)