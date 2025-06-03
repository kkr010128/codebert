a,b=map(int,input().split())
s=list(map(int,input().split()))
ans=0
s=sorted(s)
for i in range(b):
  ans+=s[i]
print(ans)
