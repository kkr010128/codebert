n=int(input())
s=[int(x) for x in list(input())]
ans=0
for a in range(10):
  for i in range(n):
    if s[i]==a:
      a_dx=i
      break
  else:
    continue
  for b in range(10):
    for i in range(a_dx+1,n):
      if s[i]==b:
        b_dx=i
        break
    else:
      continue
    for c in range(10):
      for i in range(b_dx+1,n):
        if s[i]==c:
          ans+=1
          break
      else:
        continue

print(ans)