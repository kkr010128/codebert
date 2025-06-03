S=input()
flag=0
if S==S[::-1]:
  s = S[:(len(S)-1)//2]
  if s==s[::-1]:
    s2 = S[(len(S)+3)//2-1:]
    if s2==s2[::-1]:
      flag=1
if flag:print('Yes')
else:print('No')