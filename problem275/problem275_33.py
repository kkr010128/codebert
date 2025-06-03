x,y=map(int,input().split())
dict={1:300000,2:200000,3:100000}
if x==1 and y==1:
  print(1000000)
else:
  if x<=3 and y<=3:
    print(dict[x]+dict[y])
  elif x<=3:
    print(dict[x])
  elif y<=3:
    print(dict[y])
  else:
    print(0)