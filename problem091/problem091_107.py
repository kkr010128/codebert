n=int(input())
L=list(map(int,input().split()))
a=0
for i in range(n-2):
    for j in range(i+1,n-1):
        if L[i]!=L[j]:
            for k in range(j+1,n):
                
                
                if L[i]!=L[k] and L[j]!=L[k] and L[i]<L[j]+L[k] and L[j]<L[i]+L[k] and L[k]<L[j]+L[i]:
                    a+=1
                    
                    

print(a)