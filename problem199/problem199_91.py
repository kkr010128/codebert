S = str(input())
ans = 'Yes'

from collections import Counter
SC = Counter(list(S))
h,i = 0,0
for a,b in SC.items():
  if a == 'h':
    h = b
  elif a == 'i':
    i = b
  else:
    ans = 'No'
    break

if h == i:
  for i in range(0,len(S)-1,2):
    if S[i]+S[i+1] != 'hi':
      ans = 'No'
      break
else:
  ans = 'No'
  
print(ans)