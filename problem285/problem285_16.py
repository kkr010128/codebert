s=input()
sl=len(s)
a=[]
count=1
for i in range(sl-1):
    if s[i+1]==s[i]:
        count+=1
    else:
        a.append(count)
        count=1
a.append(count)
ans=0
al=len(a)
if s[0]=="<":
    for i in range(0,al-1,2):
        m,n=max(a[i],a[i+1]),min(a[i],a[i+1])
        ans+=(m*(m+1)+n*(n-1))/2
    if al%2==1:
        ans+=a[-1]*(a[-1]+1)/2
elif s[0]==">":
    ans+=a[0]*(a[0]+1)/2
    for i in range(1,al-1,2):
        m,n=max(a[i],a[i+1]),min(a[i],a[i+1])
        ans+=(m*(m+1)+n*(n-1))/2
    if al%2==0:
        ans+=a[-1]*(a[-1]+1)/2
print(int(ans))