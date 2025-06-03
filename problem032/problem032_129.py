import math
n=int(input())
x=list(map(int,input().split(" ")))
y=list(map(int,input().split(" ")))

def minkowski(x,y,p):
    tmp=[math.fabs(x[i]-y[i])**p for i in range(len(x))]
    return sum(tmp)**(1/p)

ans=[minkowski(x,y,i) for i in range(1,4)]
ans.append(max([math.fabs(x[i]-y[i])for i in range(len(x))]))
for i in ans:
    print(i)
