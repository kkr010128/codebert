s = input()
t = input()
c = 0
ctemp = 0 

for i in range((len(s)-len(t))+1):
  for j in range(len(t)):
    if s[j+i] == t[j]:
      ctemp += 1
  c = max(c,ctemp)
  ctemp = 0
  
ans = len(t) - c
print(ans)