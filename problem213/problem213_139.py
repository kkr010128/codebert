import math
N = int(input())
x = list(map(int,input().split()))

minimum = math.inf
for i in range(101):
    stamina = 0
    for j in range(N):
        stamina += (x[j]-i)**2
    minimum = min(minimum,stamina)

print(minimum)