import math
N = int(input())

for i in range(N+1):
    if math.floor(1.08 * i) == N:
        print(i)
        exit()

print(":(")
