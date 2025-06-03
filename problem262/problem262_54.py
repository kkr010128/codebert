n=int(input())
ans=[]
tes=[[] for _ in range(n)]

for j in range(n):
    a=int(input())
    for h in range(a):
        x,y=map(int,input().split())
        tes[j].append(x)
        tes[j].append(y)

for i in range(2**n):
    f=0
    m=0
    rel=[0 for _ in range(n)]
    for j in range(n):
        if (i>>j)&1:
            rel[j]=1
            m+=1
            
    
    for j in range(n):
        
        for q in range(len(tes[j])//2):
            if rel[j]==1 and tes[j][2*q+1]!=rel[tes[j][2*q]-1]:
                f=1
    if f==0:
        ans.append(m)
print(max(ans))
            
    
        
    
    
    
        
        
    
    
    
    
        
