import math
n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))
for p in [1.0, 2.0, 3.0]:
    a = 0
    for i in range(n):
        a += abs(x[i] - y[i]) ** p
    D = a ** (1/p)
    print(D)
inf_D = float("-inf")
for i in range(n):
    if abs(x[i] - y[i]) > inf_D:
        inf_D = abs(x[i] - y[i])
print(inf_D)
