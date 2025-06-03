a,b,c,d=map(int,input().split(' '))
if a>=0:
  if d<=0:
    ans=a*d
  else:
  	x=b
  	y=d
  	ans=b*d
elif a<=0 and b>=0:
  if c>=0:
    x=b
    y=d
    ans=b*d
  elif c<=0 and d>=0:
      ans=max(a*c,b*d)
  else:
    ans=a*c
else:
  if c>=0:
    ans=b*c
  else:
    ans=a*c
print(ans)