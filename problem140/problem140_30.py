t=input()

tla=list(t)
tlb=list(t)
pd1=0
pd2=0

for i in range(len(tla)):
  if tla[i]=="?":
    if i==0:
      pass
    elif i==len(tla)-1:
      tla[i]="D"
    elif tla[i-1]=="P":
      tla[i]="D"
    elif tla[i+1]=="D":
      tla[i]="P"
    elif tla[i+1]=="?":
      tla[i]="P"
    else:
      tla[i]="D"
  if tla[i]=="D":
    if i==0:
      pass
    elif tla[i-1]=="P":
      pd1+=1
d1=tla.count('D')
s1=d1+pd1

for i in range(len(tlb)):
  if tlb[i]=="?":
    tlb[i]="D"
  if tlb[i]=="D":
    if i==0:
      pass
    elif tlb[i-1]=="P":
      pd2+=1
d2=tlb.count('D')
s2=d2+pd2

if s1>s2:
  print(''.join(tla))
else:
  print(''.join(tlb))