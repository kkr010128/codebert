import math
count=0
n,d=map(int,input().split())
for _ in range(n):
    x,y=map(int,input().split())
    dis=math.sqrt(pow(x,2)+pow(y,2))
    if dis<=d:
        count+=1
print(count)        