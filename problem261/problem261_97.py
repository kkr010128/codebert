s = input()
if len(s) == 1:
  print(0)
  exit()
  
ans = 0  
for i in range(len(s)//2):
  if s[i] != s[(-1)*(i+1)]:
    ans += 1
  else:
    pass
  
print(ans)
