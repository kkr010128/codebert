import sys
s=input().split()
n=int(s[0]);m=int(s[1]);l=int(s[2])
a=[[0 for j in range(m)]for i in range(n)]
b=[[0 for j in range(l)]for i in range(m)]
c=[[0 for j in range(l)]for i in range(n)]
for i in range(n):
    t=input().split()
    for j in range(m):
        a[i][j]=int(t[j])
for i in range(m):
    t=input().split()
    for j in range(l):
        b[i][j]=int(t[j])
for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j]+=a[i][k]*b[k][j]
        sys.stdout.write("{0}".format(c[i][j]))
        if j==l-1:
            sys.stdout.write("\n")
        else:
            sys.stdout.write(" ")