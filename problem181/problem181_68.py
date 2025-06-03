def chk(l):
  s=0
  for r in l:
    s+=r
    if (s<0)|(s>9):
      return False
  return True
def nml(l):
  ln=len(l)
  for i in range(1,ln):
    if l[-i]==2:
      l[-i]=-1
      l[-i-1]+=1
  if l[0]==10:
    return True
  return False


a=[1]
for i in range(int(input())-1):
  while True:
    if len(a)==1:
      a[0]+=1
      if a[0]==10:
        a=[1,-1]
    else:
      a[-1]+=1
      if nml(a):
        a=[1]+[-(j==0) for j in range(len(a))]
    if chk(a):
      break
rt=""
ss=0
for i in a:
  ss+=i
  rt+=str(ss)
print(rt)