s=list(input())
n=len(s)
k=int(input())
count=[]
i=0
while i<=n-1:
    j=0
    while i+j+1<=n-1 and s[i+j]==s[i+j+1]:
        j+=1
    count.append(j+1)
    i+=(j+1)

length=len(count)
if length==1:
    print((n*k)//2)
   
else:
    if s[0]==s[-1]:
        ans=0
        for l in range(length):
            if l!=0 and l!=length-1:
                ans+=(count[l]//2)*k
        ans+=(count[0]//2+count[-1]//2)
        ans+=((count[0]+count[-1])//2)*(k-1)
        print(ans)
    else:
        ans=0
        for m in count:
            ans+=(m//2)*k
        print(ans)

