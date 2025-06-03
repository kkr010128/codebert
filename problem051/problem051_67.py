while 1:
   H, W = map(int, raw_input().split())
   if H == 0 and W == 0:
      break
   else:
      for i in range(H):
         ans = ""
         for j in range(W):
            if (i+j)%2 == 0:
               ans += "#"
            else:
               ans += "."
         print ans
      print ("")