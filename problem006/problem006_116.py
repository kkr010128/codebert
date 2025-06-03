import math
n=int(input())
x=100000
for i in range(n):
    x=x*1.05
   # print('5%',x)
    x=x/1000
    #print('/1000',x)
    x=math.ceil(x)
    #print('cut',x)
    x=x*1000
    #print('*1000',x)
print(x)