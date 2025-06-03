import math
N,D = map(int,input().split())
x = [0] * N
y = [0] * N
cnt=0
for i in range(N):
    x[i], y[i] = map(int, input().split())
    if math.sqrt(x[i]**2 + y[i]**2) <= D:
        cnt +=1
print(cnt)