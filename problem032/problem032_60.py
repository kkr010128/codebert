import math
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
xy = []
for i in range(n):
    xy.append(abs(x[i] - y[i]))
D = [0, 0, 0, 0]
D[0] = sum(xy)
D2 = 0
for xyi in xy:
    D2 += xyi ** 2
D[1] = math.sqrt(D2)
D3 = 0
for xyi in xy:
    D3 += xyi ** 3
D[2] = math.pow(D3, 1.0/3.0)
D[3] = max(xy)
for d in D:
    print(d)
