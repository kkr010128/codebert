import math
N, D= list(map(int,input().split()))
cnt = 0
for i in range(N):
    x, y = list(map(int, input().split()))
    #print(math.sqrt((x^2)+(y^2)))
    if math.sqrt((x*x)+(y*y)) <= D:
        cnt+=1
        
print(cnt)