import math
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

d_1 = 0
d_2 = 0
d_3 = 0
d_4 = []
for i in range(n):
    d_1 += abs(x[i] - y[i])
    d_2 += abs(x[i] - y[i]) ** 2
    d_3 += abs(x[i] - y[i]) ** 3
    d_4.append(abs(x[i] - y[i]))
print("{0:8f}".format(d_1))
print("{0:8f}".format(math.sqrt(d_2)))
print("{0:8f}".format(d_3 ** (1/3)))
print("{0:8f}".format(max(d_4)))