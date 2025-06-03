n=int(input())
s=input()
ans=0
alist=[0]*10
for i in range(n):
  alist[int(s[i])]=i
for i in range(10):
  flag1=False
  for a in range(n-2):
    if s[a]==str(i):
      flag1=True
      break
  if flag1:
    for j in range(10):
      flag2=False
      for b in range(a+1,n-1):
        if s[b]==str(j):
          flag2=True
          break
      if flag2:
        for k in range(10):
          if b<alist[k]:
            ans+=1
print(ans)