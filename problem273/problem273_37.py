n,k=map(int,input().split())
a=list(map(lambda x:(int(x)-1)%k,input().split()))
s=[0]
for i in a:
    s.append((s[-1]+i)%k)
mp={}
ans=0
for i in range(len(s)):
    if i-k>=0:
        mp[s[i-k]]-=1
    if s[i] in mp:
        ans+=mp[s[i]]
        mp[s[i]]+=1
    else:
        mp[s[i]]=1
print(ans)
