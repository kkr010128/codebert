n,d = map(int,input().split())
su = 0
for i in range(n):
  x,y = map(int,input().split())
  #print("i=",i,"x,y=",x,y)
  if d**2 >= x**2 +y**2:
    su +=1
  else:
    continue
print(su)