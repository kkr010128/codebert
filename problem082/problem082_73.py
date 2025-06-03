s=input()
t=input()
lt=len(t);ls=len(s)
ans=lt
for i in range(ls-lt+1):
    cnt=0
    for j in range(len(t)):
        if s[i:i+lt][j]!=t[j]:
            cnt+=1
    ans=min(ans,cnt)
print(ans)