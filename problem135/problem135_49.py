A, B=input().split()
a=int(A)
R,E=B.split('.')
while len(E)<2:
    E=E+0
c=int(R+E)
p=str(a*c)
if len(p)<=2:
    print(0)
else:
    print(p[0:len(p)-2])
