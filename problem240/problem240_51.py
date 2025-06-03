n,m=map(int,input().split())
res=[[]for _ in range(n+1)]
a=0
w=0
for i in range(m):
    p,s=input().split()
    p=int(p)
    res[p].append(s)

for i in range(1,n+1):
    if "AC" in res[i]:
        a+=1
        f=0
        for j in range(len(res[i])):
            if res[i][j]=="WA" and f==0:
                w+=1
            if res[i][j]=="AC":
                f=1
        
print(a,w)
    

        


    
        
        
    
    
    
    
        
