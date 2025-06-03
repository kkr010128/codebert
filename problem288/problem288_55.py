from collections import deque
N = int(input())

p = 1
for i in range(2,int(N ** (1/2)+1)):
    if N % i == 0:
        p = i

print(int(p+N/p)-2) 
