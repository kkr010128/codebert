import math



n = int(input())

x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

p1 = 0
p2 = 0
p3 = 0
p4 = []
for i in range(n):
    p1 += math.pow(abs(x[i]-y[i]),1)

for i in range(n):
    p2 += math.pow(abs(x[i]-y[i]),2)

for i in range(n):
    p3 += math.pow(abs(x[i]-y[i]),3)
for i in range(n):
    p4.append(abs(x[i]-y[i]))

print(p1)
print(math.sqrt(p2))
print(math.pow((p3),1/3))
print(max(p4))

