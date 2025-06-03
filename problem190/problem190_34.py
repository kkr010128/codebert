s=input()
n=len(s)
s1=s[:(n-1)//2]
s2=s[(n+3)//2-1:]

def check(s):
  i=0
  j=len(s)-1
  while j>i:
    if s[j]!=s[i]:
      return False
    j-=1
    i+=1
  return True

if check(s) and check(s1) and check(s2):
  print("Yes")
else:
  print("No")