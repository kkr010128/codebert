import math
N = int(input())

min = math.floor(N / 1.08)
max = math.ceil(N/ 1.08)
flag = False
for i in range(min,max+1):
    ans = math.floor(i*1.08)
    if N == ans:
        X = i
        flag = True
        break
if(flag):
    print(X)
else:
    print(':(')