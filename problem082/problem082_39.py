s=input()
t=input()
c=len(t)
for i in range(len(s)-len(t)+1):
  d=0
  for j in range(len(t)):
    if s[i+j]!=t[j]:
      d+=1
  if d<c:
    c=d
print(c)