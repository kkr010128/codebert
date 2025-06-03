X=int(input())
A=[]
i,p=0,True
while p:
  a=i**5
  A.append(a)
  for b in A:
    if a-b==X:
      p=False
      print(i,A.index(b))
      break
    elif a+b==X:
      p=False
      print(i,-1*A.index(b))
      break
  i+=1