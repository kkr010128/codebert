n=int(input())
if n<3:
  print(0)
else:
  L=[int(i) for i in input().split()]
  x=0
  for i in range(0,n-2):
    for j in range(i+1,n-1):
      for k in range(j+1,n):
        if L[i]==L[j] or L[j]==L[k] or L[k]==L[i]:
          pass
        elif L[i]+L[j]>L[k] and L[i]+L[k]>L[j] and L[j]+L[k]>L[i]:
          x+=1
        else:
          pass
  print(x)