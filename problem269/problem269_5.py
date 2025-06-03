T1,T2,A1,A2,B1,B2=map(int,open(0).read().split())
D1,D2=(A1-B1)*T1,(A1-B1)*T1+(A2-B2)*T2
if D1*D2>0:print(0)
elif D2==0:print("infinity")
else:print(-D1//D2*2+1-(-D1%D2==0))