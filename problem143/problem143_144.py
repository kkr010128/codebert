k=int(input())
s=input()

l=len(s)

if l<=k:
  print(s)
else:
  s=list(s)
  t=[]
  for i in range(k):
    t.append(s[i])
  t.append('...')
  print(''.join(t))
