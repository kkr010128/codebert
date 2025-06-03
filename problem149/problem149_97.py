import sys
n,m,x=map(int,input().split())
ac=[[0]*(m+1) for i in range(n)]
a=[[0]*m for i in range(0,n)]
c=[0 for i in range(n)]
for i in range(n):
  ac[i]=list(map(int,input().split()))
  c[i]=ac[i][0]
  a[i]=ac[i][1:m+1]#sliceは上限+１を:の右に代入
cheap=[]
kaukadouka=[0 for i in range(n)]

def kau(i):
  global a,x,kaukadouka,cheap,c
  rikaido=[0 for i in range(m)]#初期化
  for j in range(i+1,n):
    kaukadouka[j]=0
  if i>=n:
      sys.exit()
  kaukadouka[i]=1
  for j in range(n):
    for k in range(m):
      rikaido[k]+=kaukadouka[j]*a[j][k]
  value=0
  if min(rikaido)>=x:
    for j in range(n):
      value+=c[j]*kaukadouka[j]
    cheap.append(value)
  if i<n-1:
    kau(i+1)
    kawanai(i+1)
    
def kawanai(i):
  global kaukadouka
  for j in range(i,n):
    kaukadouka[j]=0

  if i>=n:
    sys.exit()
  #print('i=',i,'のとき買わないで')
  #print('->',kaukadouka)

  if i<n-1:
    kau(i+1)
    kawanai(i+1)

kau(0)
kawanai(0)
if len(cheap)>0:
	#print(cheap)
	print(min(cheap))
else:
  print('-1')