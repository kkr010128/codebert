a,b,c =map(int, input().split())
if a<b and b<c:
  print(a,b,c)
elif a>b:
  if b>=c:
    a,c = c,a
    print(a,b,c)
  else:
    a,b = b,a
    b,c = c,b
    print(a,b,c)
else:
  if a>c:
    a,b = b,a
    a,c = c,a
    print(a,b,c)
  else:
    b,c = c,b
    print(a,b,c)
