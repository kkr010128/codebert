from math import sqrt
n=int(input())
while 1:
    k=0
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            k=1
            break
    if(k==0):
            print(n)
            break
        
    n+=1
