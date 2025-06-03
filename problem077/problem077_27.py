L=list(map(int,input().split()))
a=L[0]
b=L[1]
c=L[2]
d=L[3]
print(max(a*c,b*d,a*d,b*c))