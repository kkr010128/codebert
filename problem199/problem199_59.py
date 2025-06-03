S = input()

ans = 'Yes'
while len(S) > 0:
  if S[:2] == 'hi':
    S = S[2:]
  else:
    ans = 'No'
    break

print(ans)