n=int(input())
x=int(100000)
for i in range(1,n+1) :
    x = x*1.05
    if x%1000 == 0 :
        continue
    
    else :
        x = x//1000*1000+1000
        
print("{:.0f}".format(x))
        
