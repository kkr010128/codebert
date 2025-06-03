import math
a = int(input())
answer = 100000000
b = list(map(int,input().split()))
for i in range(1,101):
    cost = 0
    for j in b:
        cost+=(j-i)**2
    answer = min(answer,cost)
print(answer)