while True:
   x=input()
   if x=="0":
       break
   cnt = 0
   for i in x:
       num = int(i)
       cnt += num
   print(cnt)