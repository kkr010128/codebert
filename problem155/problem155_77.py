n,m=map(int,input().split())
h=list(map(int,input().split()))
final=[1]*n
for i in range(m):
  a,b=map(int,input().split())
  if h[a-1]<h[b-1]:
         final[a-1]=0
  elif h[a-1]>h[b-1]:
         final[b-1]=0
  else:
         final[a-1]=0
         final[b-1]=0
print(sum(final))