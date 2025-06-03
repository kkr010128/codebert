import math
N = int(input())
for i in range(math.floor(N**0.5),0,-1):
    if N%i==0:
        print(i+N//i-2)
        exit()
