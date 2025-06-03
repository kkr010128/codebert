n = int(input())
m = 0
a = n // 3
b = n // 5
c = n // 15
for i in range(1,n+1):
    m = m+i
for j in range(1,a+1):
    m = m-(3*j)
for k in range(1,b+1):
    m = m-(5*k)
for l in range(1,c+1):
    m = m+(15*l)
print(m)