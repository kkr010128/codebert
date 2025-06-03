s = input()

def check():
  if s != s[::-1]:
    return("No")
  n = len(s)
  s1 = s[:int((n-1)/2)]
  #print(s1)
  if s1 != s1[::-1]:
    return("No")
  s2 = s[int((n+3)/2-1):]
  if s2 != s2[::-1]:
    return("No")
  #print(s2)
  return("Yes")

print(check())