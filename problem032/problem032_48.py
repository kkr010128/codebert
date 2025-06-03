import math
n = int(input())
x = [int(num) for num in input().split()]
y = [int(num) for num in input().split()]
D1 = 0
D2 = 0
D3 = 0
D4 = []
for i, j in zip(x, y):
    D1 += abs(i - j)
print(D1)
for i, j in zip(x, y):
    D2 += (abs(i - j))**2
print(math.sqrt(D2))
for i, j in zip(x, y):
    D3 += (abs(i - j))**3
print(math.pow(D3, 1.0/3.0))
for i, j in zip(x, y):
    D4.append(abs(i - j))
print(max(D4))