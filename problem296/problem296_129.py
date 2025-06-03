s=input()
n=len(s)
k=int(input())
if s[0]==s[n-1]:
  d=1
  ans=0
  for i in range(1,n):
    if s[i-1]==s[i] and d==1:
      ans+=1
      d=0
    elif s[i-1]==s[i] and d==0:
      d=1
    elif s[i-1]!=s[i]:
      d=1
  if d==0:
    print(ans*k)
  else:
    ans2=0
    for i in range(n):
      if s[i-1]==s[i] and d==1:
        ans2+=1
        d=0
      elif s[i-1]==s[i] and d==0:
        d=1
      elif s[i-1]!=s[i]:
        d=1
    if d==1:
      print(ans+ans2*(k-1))
    else:
      if k%2==0:
        print((ans+ans2)*k//2)
      else:
        print((ans+ans2)*(k//2)+ans)
elif s[0]!=s[n-1]:
  d=1
  ans=0
  for i in range(1,n):
    if s[i-1]==s[i] and d==1:
      ans+=1
      d=0
    elif s[i-1]==s[i] and d==0:
      d=1
    elif s[i-1]!=s[i]:
      d=1
  print(ans*k)