s=input().split()
n=int(s[0])
m=int(s[1])
a=[[0 for j in range(m)]for i in range(n)]
b=[0 for j in range(m)]
for i in range(n):
    t=input().split()
    for j in range(m):
        a[i][j]=int(t[j])
for j in range(m):
    b[j]=int(input())
c=[0 for i in range(n)]
for i in range(n):
    for j in range(m):
        c[i]+=a[i][j]*b[j]
    print("{0}".format(c[i]))