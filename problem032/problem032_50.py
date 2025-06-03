#10_D
import math
n=int(input())
x_v=list(map(int,input().split()))
y_v=list(map(int,input().split()))

p=1
while(p<5):
    d=0
    if(p==4):
        my_list=[]
        for i in range(n):
            my_list.append(abs(x_v[i]-y_v[i]))
        d=max(my_list)
        print(d)
    else:
        for i in range(n):
            d+=abs(x_v[i]-y_v[i])**p
        d=pow(d,1/p)
        print(d)
    p+=1
