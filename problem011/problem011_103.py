#16D8101023J 久保田凌弥 kubotarouxxx python3

x,y=map(int, input().split())

if x>y:
  while 1:
   if (x%y)==0:
    print(y)
    break
   a=x%y
   x=y
   y=a
else:
  while 1:
   if (y%x)==0:
    print(x)
    break
   a=y%x
   y=x
   x=a

