s=list(input())
l=len(s)
ans=0

if len(set(s))==1:
    for i in range(1,l+1):
        ans+=i
    print(ans)
    exit()

for i in range(l-1):
    if s[i]=="<" and s[i+1]==">":
        left=1
        right=1
        for j in range(i):
            if s[i-j-1]=="<":
                left+=1
            else:
                break
        for j in range(l-i-2):
            if s[i+j+2]==">":
                right+=1
            else:
                break
        p=max(left,right)
        q=min(left,right)
        for j in range(p):
            ans+=(j+1)
        for j in range(q-1):
            ans+=(j+1)
if s[0]==">":
    ans+=1
    for i in range(1,l):
        if s[i]==">":
            ans+=(i+1)
        else:
            break
if s[-1]=="<":
    ans+=1
    for i in range(2,l+1):
        if s[-i]=="<":
            ans+=i
        else:
            break
print(ans)