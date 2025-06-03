S = input()
T = input()

lens = len(S)
lent = len(T)

ans = lent

for i in range(lens - lent + 1):
  count = 0
  for j in range(lent):
    if S[i+j] != T[j]:
      count = count + 1

  if count < ans:
    ans = count
    
print(ans)
