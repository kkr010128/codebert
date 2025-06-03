x=int(input())
i=0
while True:
  360*i%x!=0
  i+=1
  if 360*i%x==0:
    break
k=360*i/x
print(int(k))
