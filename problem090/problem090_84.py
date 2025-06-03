s = input().rstrip()
best = 0
c = 0

for char in s:
  if char=='R':
    c+=1
  else:
    c=0
    
  best = max(best,c)
  
print(best)