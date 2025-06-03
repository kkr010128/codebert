n=int(input())
x=list(input())
def str2int(z):
  flag=1
  a=0
  for i in reversed(x):
    if i=='1':a+=flag
    flag*=2
  return a
 
popc=x.count('1')
z=str2int(x)
if popc-1!=0:
  fl_1=z%(popc-1)
fl_0=z%(popc+1)

for i in range(n):
  if x[i]=='1':
    if popc-1==0:
      print(0)
      continue
    mod=(fl_1-pow(2,n-1-i,popc-1))%(popc-1)
  else:mod=(fl_0+pow(2,n-1-i,popc+1))%(popc+1)
  #print('mod : %s'%mod)
  cnt=1
  while mod!=0:
    pp=bin(mod).count("1")
    mod%=pp
    cnt+=1
  print(cnt)