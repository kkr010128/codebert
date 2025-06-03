N=int(input())
S=[]
T=[]
for i in range(N):
  x,y=map(str,input().split())
  S.append(x)
  T.append(int(y))
X=str(input())
p=S.index(X)
print(sum(T[p+1:]))