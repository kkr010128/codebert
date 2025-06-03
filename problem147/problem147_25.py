S = input()
T = input()
ans = ''

if len(T) != len(S) + 1:
  ans = 'No'
else:
  ans = 'Yes'

for i in range(len(S)):
  if S[i] != T[i]:
    ans = 'No'    

print(ans)