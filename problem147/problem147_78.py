S = input()
T = input()
ans = "Yes"
for i in range(len(S)):
  if S[i] != T[i]:
    ans = "No"
print(ans)