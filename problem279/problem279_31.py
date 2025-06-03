N=int(input())
S=input()
if N%2==1:print('No')
else:
  s1,s2=S[:N//2],S[N//2:]
  ok=1
  for i in range(N//2):
    if s1[i]!=s2[i]:
      print('No')
      ok=0
      break
  if ok==1:print('Yes')