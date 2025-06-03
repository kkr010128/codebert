t=input()
ans=str()
tmp=""
for s in t:
    if s=="P" or s=="D":
        ans+=s
        tmp=s
    else:
        ans+="D"
        tmp="D"

print(ans)