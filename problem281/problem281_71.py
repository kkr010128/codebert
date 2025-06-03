X,Y=map(int,input().split())
mod=10**9+7
if (X+Y)%3!=0:
  print(0)
else:
  N=int((2*Y-X)/3)
  M=int((2*X-Y)/3)
  if N<0 or M<0:
    print(0)
  if N==0 or M==0:
    print(1)
  if N>0 and M>0:
    List=[0 for i in range(N+M)]
    List[0]=1
    for i in range(N+M-1):
      List[i+1]=List[i]*(i+2)%mod
    print(List[N+M-1]*pow(List[N-1],mod-2,mod)*pow(List[M-1],mod-2,mod)%mod)