a=int(input())
b,c=input().split()
b=int(b)
c=int(c)
if b%a==0 or c%a==0:
  print("OK")
else:
  if int(b/a)==int(c/a):
    print("NG")
  else:
    print("OK")