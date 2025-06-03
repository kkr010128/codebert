a,s=0,input().lower()
while(True):
  t = input().split()
  if t[0] == "END_OF_TEXT":
    print(a)
    quit()
  for i in t:
    if i.lower() == s:
      a += 1
