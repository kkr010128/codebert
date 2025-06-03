import math , sys
N = int( input() )

X = []
for i in range(N):
    A , B = list(map(int, input().split()))
    X.append([i , A-B , A , A+B])


X.sort(key=lambda x: x[3])

Y = X[0]
Ri = Y[-1]
ans = 1

j=0

for i in range(1,N):
    Y = X[i]
    if Y[1] >= Ri:
        ans+=1
        Ri = Y[-1]
print(ans)
