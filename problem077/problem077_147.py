a=input('').split()
a=list(map(int,a))

b=(a[0])
c=(a[1])
d=(a[2])
e=(a[3])

f=b*d
g=b*e
h=c*d
i=c*e

if f>g:
  if h>f:
    if i>h:
      print(i)
    else:
      print(h)
  else:
    if i>f:
      print(i)
    else:
      print(f)
else:
  if h>g:
    if i>h:
      print(i)
    else:
      print(h)
  else:
    if i>g:
      print(i)
    else:
      print(g)
