x = 1
y = 1
while x != 0 or y != 0:
 n = map(int,raw_input().split())
 x = n[0]
 y = n[1]
 if x == 0 and y == 0:
  break
 elif x <= y:
  print x,y
 elif x >  y:
  print y,x