s=input()
k=int(input())
cnt=1
temp=[]
for i in range(len(s)-1):
    if s[i]==s[i+1]: cnt+=1
    else:
        temp.append([s[i],cnt])
        cnt=1
if cnt>=1: temp.append([s[-1],cnt])
if len(temp)==1:
    print(k*len(s)//2)
    exit()
ans=0
if temp[0][0]!=temp[-1][0]:
    for pair in temp:
        if pair[1]!=1: ans+=pair[1]//2
    print(ans*k)
else:
    for pair in temp[1:-1]:
        if pair[1]!=1: ans+=pair[1]//2
    ans*=k
    ans+=(k-1)*((temp[0][1]+temp[-1][1])//2)
    ans+=temp[0][1]//2+temp[-1][1]//2
    print(ans)