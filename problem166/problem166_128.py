s=list(input())
mod=2019
mdict={}
mdict[0]=1
ans=0
tmp=0
for i in range(len(s)):
    n=s.pop()
    key=(int(n)*pow(10,i,mod)+tmp)%mod

    if key in mdict:
        mdict[key]+=1
    else:
        mdict[key]=1
    tmp=key

for var in mdict.values():
    ans+=var*(var-1)//2

print(ans)