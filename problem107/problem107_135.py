def f(n):
  ans=1
  while n!=0:
    ans+=1
    n%=bin(n).count("1")
  return ans
n=int(input())
x=input()
o=x.count("1")
if o==0:exit(print(*[1]*n))
if o==1:
  if x[-1]=="1":
    ans=[2]*n
    ans[-1]=0
  else:
    ans=[1]*n
    ans[-1]=2
    ans[x.index("1")]=0
  exit(print(*ans))
mo=0
mz=0
for i in range(n):
  if x[n-i-1]=="1":
    mo=(pow(2,i,o+1)+mo)%(o+1)
    mz=(pow(2,i,o-1)+mz)%(o-1)
for i in range(n):
  if x[i]=="1":
    m=(mz-pow(2,n-i-1,o-1))%(o-1)
  else:
    m=(mo+pow(2,n-i-1,o+1))%(o+1)
  print(f(m))