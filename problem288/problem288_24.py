from math import sqrt
n=int(input())
m=int(sqrt(n)//1)

for i in range(m,0,-1):
    if n%i==0:
        m=i
        o=n//m
        break
print(m+o-2)