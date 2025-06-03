a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
ls=[a,b,c]
ls.sort()
if ls[0]==ls[1]:
  if ls[1]==ls[2]:
    print("No")
  else:
    print("Yes")
else:
  if ls[1]==ls[2]:
    print("Yes")
  else:
    print("No")