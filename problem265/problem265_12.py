import math

n = int(input())
for i in range(n+1):
    if math.floor(i * 1.08) == n:
        print(i)
        exit(0)
print(":(")