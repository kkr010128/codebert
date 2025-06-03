n,k=map(int,input().split())
a=list(map(int,input().split()))
a.append(0)
s=input()
ans=0
for i in range(k,n):
  if s[i]==s[i-k]:
    s=s[:i]+'z'+s[i+1:]
for i in range(n):
  ans+=a['sprz'.index(s[i])]
print(ans)