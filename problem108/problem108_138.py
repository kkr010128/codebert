N=int((input()))

if N%1000==0:
    print(0)
    
else:
  N=str(N)
  a = len(N)
  if a>=3:
        x = int(N[a-3]+N[a-2]+N[a-1])
        print(1000-x)
  elif a==2:
        x = int(N[a-2]+N[a-1])
        print(1000-x)
  else :
        x = int(N[a-1])
        print(1000-x)