while 1:
   H, W = map(int,raw_input().split())

   if H ==0 and W == 0:
      break
   for i in range(H):
      if i%2==0:
        if W%2==0:
           print "#."*(W/2)
        elif W%2==1:
           print "#."*(W/2)+"#"
      elif i%2==1:
         if W%2==0:
            print ".#"*(W/2)
         elif W%2==1:
            print ".#"*(W/2)+"."
   print ""