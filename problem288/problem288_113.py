import math
N = int(input())

n = int(math.sqrt(N))

ans = 0
l = []
for i in range(1,2*n):
    if int(N/i) == N/i:
        l.append(i+N/i-2) 

print(int(min(l)))