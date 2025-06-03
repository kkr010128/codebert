L= list(map(int,input().split()))
a=1
for i in range(5):
  if L[i]!=0:
    a+=1
  else:
    print(a)
