W,H,x,y,r=map(int,input().split())

a = x-r
b = x+r

c = y-r
d = y+r 

  
if a>=0 and b<=W and c>=0 and d<=H:
  print("Yes") 

else:
    print("No")
