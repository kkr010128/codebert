import math
N = int(input())
for i in range(1,N+1):
    if math.floor(i*1.08) == N:
        print(i)
        break
else:
    print(":(")