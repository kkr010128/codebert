import math

n = int(input())
x_buf = input().split()
y_buf = input().split()

x = []
y = []
for i in range(n):
    x.append(int(x_buf[i]))
    y.append(int(y_buf[i]))

sum1 = 0
sum2 = 0
sum3 = 0
sum_inf = 0
max_inf = 0
for i in range(n):
    sum1 += abs(x[i] - y[i])
    sum2 += abs(x[i] - y[i]) ** 2
    sum3 += abs(x[i] - y[i]) ** 3
    sum_inf = abs(x[i] - y[i])
    if max_inf < sum_inf:
        max_inf = sum_inf

d1 = sum1
d2 = math.sqrt(sum2)
d3 = sum3 ** (1/3)
d4 = max_inf

print(d1)
print(d2)
print(d3)
print(d4)

