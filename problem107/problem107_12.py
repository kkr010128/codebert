N=int(input())
X=input()
A=[0,1,1,2,1,2,1,2,1,2,1,2,1,2,2,3,1]

ppx=0

for i in range(N):
  if X[i]=="1":
    ppx+=1
if ppx<=1:
  ppxm1=1
else:
  ppxm1=ppx-1
Xmod=[0,0]
XmodP=[0]*N
XmodM=[0]*N
XmodP[0]=1%(ppx+1)
XmodM[0]=1%(ppxm1)
Xmod=[XmodP[0]*(X[-1]=="1"),XmodM[0]*(X[-1]=="1")]
for i in range(N-1):
  XmodP[i+1]=(XmodP[i]*2)%(ppx+1)
  XmodM[i+1]=(XmodM[i]*2)%(ppxm1)
  if X[-2-i]=="1":
    Xmod[0]=(Xmod[0]+XmodP[i+1])%(ppx+1)
    Xmod[1]=(Xmod[1]+XmodM[i+1])%(ppxm1)
for i in range(N):
  if X[i]=="0":
    Xm=(Xmod[0]+XmodP[-1-i])%(ppx+1)
  else:
    Xm=(Xmod[1]-XmodM[-1-i])%(ppxm1)
  if ppx==1 and X[i]=="1":
    print(0)
  elif Xm==0:
    print(1)
  else:
    px=0
    temp=Xm
    while temp>0:
      if temp%2==1:
        px+=1
        temp=(temp-1)/2
      else:
        temp=temp/2
    p=Xm%px
    print(A[p]+2)