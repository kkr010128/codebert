import math
n = int(input())
s = input().split(" ")
x = list(map(int,s))
s = input().split(" ")
y = list(map(int,s))
sa = []
for i in range(n):
    sa.append(math.fabs(x[i]-y[i]))
goukei = 0
for i in range(n):
    goukei += sa[i]
p1 = goukei
print(p1)
goukei = 0
for i in range(n):
    goukei += sa[i]**2
p2 = math.sqrt(goukei)
print(p2)
goukei = 0
for i in range(n):
    goukei += sa[i]**3
p3 = math.pow(goukei,1/3)
print(p3)
saidaisa = 0
for i in range(n):
    if sa[i] > saidaisa:
        saidaisa = sa[i]
print(saidaisa)