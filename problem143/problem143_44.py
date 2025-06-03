k=int(input())
s=list(input())
if len(s)<=k:
  print("".join(s))
else:
  s_short=""
  for i in range(k):
    s_short+=s[i]
  print((s_short+"..."))