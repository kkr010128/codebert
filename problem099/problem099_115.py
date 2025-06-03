N,K=[int(s) for s in input().split()]
maruta=[int(s) for s in input().split()]

def possible(x):
  cut=0
  for e in maruta:
    if e%x==0:
      cut+=(e//x-1)
    else:
      cut+=e//x
  if cut<=K:
    return True
  else:
    return False

a=1
b=max(maruta)
while b-a>1:
  c=(a+b)//2
  if possible(c):
    b=c
  else:
    a=c

if possible(1):
  print(1)
else:
  print(b)
