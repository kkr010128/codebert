import math
N,D = map(int,input().split())

cnt=0

for i in range(N):
    X,Y = map(int,input().split())
    
    dis = math.sqrt(X*X+Y*Y)

    if dis <= D:
        cnt+=1
        
        
print(cnt)