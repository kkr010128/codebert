while 1:
   x,y = map(int, raw_input().split())
   if x == 0 and y == 0:
      break
   if y >= x:
      print '%s %s' % (x, y)
   else:
      print '%s %s' % (y, x)