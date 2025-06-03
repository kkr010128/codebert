n=int(input())
i=0
x=100000
for i in range(n):
    x=int(x*1.05)
    if x%1000==0:
        x=x
    else:
        x=x+1000-x%1000
    i+=1
    
print(x)
