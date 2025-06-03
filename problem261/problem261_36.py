s=list(input())
ans=0
for i in range(len(s)//2):
    if s[i]==s[len(s)-1-i]:
        continue
    ans+=1
print(ans)