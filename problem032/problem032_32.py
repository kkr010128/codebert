import math
n=int(input())
a=[]
for i  in range(2):
    s = list(map(int, input().split()))
    a.append(s)
d1=0
for i in range(n):
    d1+=abs(a[0][i-1]-a[1][i-1])
print(format(d1, '.6f'))
d2_1=0
for i in range(n):
    d2_1+=(abs(a[0][i-1]-a[1][i-1]))**2
d2=math.sqrt(d2_1)
print(format(d2, '.6f'))
d3_1=0
for i in range(n):
    d3_1+=(abs(a[0][i-1]-a[1][i-1]))**3
d3=(d3_1)**(1/3)
print(format(d3, '.6f'))
dn=0
for i in range(n):
    dn=max(abs(a[0][i-1]-a[1][i-1]),dn)
print(format(dn, '.6f'))
