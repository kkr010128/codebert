s=str(input())
k=int(input())
ans=0
count=1
c1=0
c2=0

if len(set(s))==1:
    print(len(s)*k//2)
    exit()

if s[0]==s[-1]:
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            if 2<=count:
                ans+=count//2
            count=1
    ans+=count//2
    i=0
    while s[i]==s[0]:
        c1+=1
        i+=1
    
    i=len(s)-1
    while s[i]==s[-1]:
        c2+=1
        i-=1
    #print(c1,c2)
    ans*=k
    if c1%2==1 and c2%2==1:
        ans+=k-1

    print(ans)


else:
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            if 2<=count:
                ans+=count//2
            count=1
    ans+=count//2
    print(ans*k)