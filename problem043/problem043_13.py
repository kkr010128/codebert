while 1:
  x,y = map( int , raw_input().split() )
  if x == 0 and y == 0:
    break
  elif x <= y:
    print "%d %d" %(x,y) 
  elif y < x : 
    print "%d %d" %(y,x) 