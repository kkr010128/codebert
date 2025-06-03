a=input()

if len(a)==4 or len(a)==5:
  b=a[1:]
  c=1000-int(b)
  if c==1000 :
    print('0')
  else:
    print(c)
  
else:
  print(1000-int(a))

