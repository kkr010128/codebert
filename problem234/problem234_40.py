n=int(input())
ans=0
currentpower=0
for i in range(1,n+1):
  if i>=10**(currentpower+1):
    currentpower+=1
  b=i%10
  a=(i-i%(10**currentpower))//(10**currentpower)
  if b==0:
    continue
  if a==b:
    ans+=1
    if currentpower>0:
      ans+=2
    r=max(0,((i-(a*(10**currentpower))-b)//10))
    ans+=2*r
    for j in range(0,currentpower-1):
      ans+=2*(10**j)
  elif a<b:
    for j in range(0,currentpower-1):
      ans+=2*(10**j)
  else:
    for j in range(0,currentpower):
      ans+=2*(10**j)
print(ans)
