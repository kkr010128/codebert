a,b=map(int,input().split())
a_s=a/0.08
a_t=(a+1)/0.08
b_s=b/0.1
b_t=(b+1)/0.1

a0=int(a_s)
a1=int(a_t)
b0=int(b_s)
b1=int(b_t)


if (a_s-a0)>0:
  a0+=1
if (a_t-a1)<=0:
  a1-=1
if (b_s-b0)>0:
  b0+=1
if (b_t-b1)<=0:
  b1-=1

lista=[i for i in range(a0,a1+1)]
listb=[i for i in range(b0,b1+1)]

ansl=[]
for j in range(len(lista)):
  if lista[j] in listb:
    ansl.append(lista[j])

if not ansl==[]:
  ans=ansl[0]
  print(ans)
else:
  print(-1)