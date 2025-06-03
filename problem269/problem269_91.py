T1,T2=map(int,input().split())
a,b=map(int,input().split())
c,d=map(int,input().split())
e=T1*a
f=T1*c
if e>f:
  g=e-f
  e=T2*b
  f=T2*d
  if e>f:
    print(0)
  else:
    h=f-e
    if g==h:
      print("infinity")
    elif g>h:
      print(0)
    else:
      k=h-g
      if k>g:
        print(1)
      elif (g/k)%1!=0:
        print(1+(g//k)*2)
      else:
        print((g//k)*2)
elif e<f:
  g=f-e
  e=T2*b
  f=T2*d
  if e<f:
    print(0)
  else:
    h=e-f
    if g==h:
      print("infinity")
    elif g>h:
      print(0)
    else:
      k=h-g
      if k>g:
        print(1)
      elif (g/k)%1!=0:
        print(1+(g//k)*2)
      else:
        print((g//k)*2)