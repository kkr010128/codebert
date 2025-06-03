from math import pow,fabs

N = int(input())
X = list(map(float,input().split()))
Y = list(map(float,input().split()))

def distance(length,x,y,n):
    D = 0
    for i in range(length):
        D += fabs(x[i]-y[i]) ** n
    return pow(D,1.0/n)

def che_distance(length,x,y):
    D = 0
    for i in range(length):
        if D < fabs(x[i]-y[i]):
            D = fabs(x[i]-y[i])
    return D

p1 = distance(N,X,Y,1)
p2 = distance(N,X,Y,2)
p3 = distance(N,X,Y,3)
pinf = che_distance(N,X,Y)

print("{}\n{}\n{}\n{}".format(p1,p2,p3,pinf))
