import math
f = True
N = int(input())
for i in range(N+1):
    if math.floor(i*1.08) == N:
        print(i)
        f = False
        break
if f:
    print(":(")



