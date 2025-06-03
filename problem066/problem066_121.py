f=n=0
while 1:
 a=input()
 if a.isdigit():
  if n==1:s=s[int(a):]
  n=1
 else:
  if f==1:print(s[:l])
  if'-'==a:break
  f=1
  n=0
  l=len(a)
  s=a*100