n=int(input())
s=list(input())
# z=90=>65
for i in s:
  x=ord(i)
  y=x+n
  if y>90:
    z=chr(y-26)
  else:
    z=chr(y)
  print(z,end='')