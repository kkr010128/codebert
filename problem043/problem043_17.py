while(1):
 x,y=map(int,input().split())
 if x==0 and y==0 :
  break
 elif x<y:
  print(x,y,sep=" ")
 else :
  print(y,x,sep=" ")