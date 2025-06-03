def compare(t,s):
  diff=0
  assert len(t) == len(s)
  for i in range(len(s)):
    if s[i]!=t[i]:
      diff+=1
  return diff
 
t = input().strip()
s = input().strip()
smallchange = len(s)
assert len(t) >= len(s)
for i in range(len(t)-len(s)+1):
  x = compare(t[i:len(s)+i], s)
  if smallchange > x:
    smallchange = x
 
print(smallchange)