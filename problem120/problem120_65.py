n,k=map(int,input().split())
p=list(map(int, input().split()))

min=p[0]
for i in range(n-1) :
    for j in range(n-1-i) :
        if(p[i]>p[j+i+1]) :
            t=p[i]
            p[i]=p[j+i+1]
            p[j+i+1]=t
    
sum=0
for i in range(k) :
    sum+=p[i]

print(sum)