T1,T2,A1,A2,B1,B2=map(int, open(0).read().split())
C1,C2=A1-B1,A2-B2
if C1<0: C1,C2=-C1,-C2
Y1=C1*T1
Y2=Y1+C2*T2
if Y2>0:
    print(0)
elif Y2==0:
    print("infinity")
else:
    print(1+Y1//(-Y2)*2-(Y1%(-Y2)==0))