import math
k=int(input())
if(k%2)==0:
    print("-1")
else:
    flag=0
    for x in range(1,1000001):
        if (7%(9*k)*(pow(10,x,k*9)-1)%(9*k))==0:
            print(x)
            flag=1
            break
    if flag==0:
        print(-1)
