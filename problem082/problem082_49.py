s=input()
t=input()
n=len(s)
n1=len(t)  
ans=10**10 
for i in range(n-n1+1):
    diff=0
    for j in range(n1):
        if(t[j]!=s[i+j]):
            diff+=1
    ans=min(ans,diff)
print(ans)