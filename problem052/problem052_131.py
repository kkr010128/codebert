n=int(raw_input())
i=1
print "",
while i<=n:
  x=i
  if x%3==0:
    print i,
  else:
    while x:
      if x%10==3:
        print i,
        break
      x/=10
  i+=1