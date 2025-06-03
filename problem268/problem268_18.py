n=int(input())
a=list(map(int,input().split()))

col=[0,0,0]
res=1

for ai in a:
    cnt=0
    for i in range(3):
        if col[i]==ai:
            if cnt==0:
                col[i]=col[i]+1

            
            cnt+=1
            
    
    res=(res*cnt)%1000000007

print(res)
