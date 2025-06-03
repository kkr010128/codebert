while True:
 x,y =map(int, raw_input().split())
 if(x==0 and y==0):
   break
 elif(x>y):
  print y,x  
 elif(x<=y):
  print x,y