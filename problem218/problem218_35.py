n=int(input())
s={}
for i in range(n):
  si = input()
  if si not in s:
    s[si] = 1
  else:
    s[si]+=1
sa = sorted(s.items())
ma = max(s.values())
for a in sorted(a for a in s if s[a]==ma):
  print(a)