S=input()
ans=0
if 'R' in S:
    ans+=1
for i in range(2):
    if S[i]==S[i+1]=='R':
        ans+=1
print(ans)