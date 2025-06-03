while 1:
 a,b=map(int,input().split())
 if a+b==0:
  break
 elif a>b:
  print(b,a)
  continue
 print(a,b)