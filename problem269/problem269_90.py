T1,T2= map(int, input().split())
A1,A2= map(int, input().split())
B1,B2= map(int, input().split())
if A1>B1 and A2>B2:
  print(0)
elif A1<B1 and A2<B2:
  print(0)
elif T1*A1+T2*A2==T1*B1+T2*B2:
  print('infinity')
elif A1>B1 and A2<B2:
  if T1*A1+T2*A2>T1*B1+T2*B2:
    print(0)
  else:
    se=abs(T1*A1+T2*A2-(T1*B1+T2*B2))
    ad=T1*A1-T1*B1
    d=-(-ad//se)
    ans=2*d-1
    if ad%se==0:
      ans+=1
    print(ans)
elif A1<B1 and A2>B2:
  if T1*A1+T2*A2<T1*B1+T2*B2:
    print(0)
  else:
    se=abs(T1*A1+T2*A2-(T1*B1+T2*B2))
    ad=T1*B1-T1*A1
    d=-(-ad//se)
    ans=2*d-1
    if ad%se==0:
      ans+=1
    print(ans)
  
