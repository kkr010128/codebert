S=input()
ans=0
if 'R' in S:
    ans+=1
    if S[0]=='R' and S[1]=='R':
        ans+=1
    if S[1]=='R' and S[2]=='R':
        ans+=1
print(ans)
