import math
N = int(input())
flag = True
for i in range(N+1):
    if math.floor(i * 1.08) == N:
        print(i)
        flag = False
        break
if flag:
    print(':(')