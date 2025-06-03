#ITP1_10-D Distance2
n = int(input())
x = [float(x) for x in input().split(" ")]
y = [float(x) for x in input().split(" ")]

d1=0.0
for i in range(n):
    d1 += abs(x[i]-y[i])
print(d1)

d2=0.0
for i in range(n):
    d2 += (x[i]-y[i])**2
print(d2**(1/2))

d3=0.0
for i in range(n):
    d3 += abs((x[i]-y[i])**3)
print(d3**(1/3))

d_inf=0.0
for i in range(n):
    if abs(x[i]-y[i])>d_inf:
        d_inf = abs(x[i]-y[i])
print(d_inf)