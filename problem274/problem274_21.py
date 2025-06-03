n,m=map(int,input().split())
l=list(input())
l=l[::-1]
now=0
ans=[]
while now<n:
  num=min(n-now,m)#進める最大
  b=True
  for i in range(num):
    num1=num-i
    if l[now+num1]!="1":
      ans.append(str(num1))
      now+=num1
      b=False
      break
  if b:
    now=n+1
if b:
  print(-1)
else:
  ans=ans[::-1]
  print(" ".join(ans))