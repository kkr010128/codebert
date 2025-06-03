S = input()
T = input()

ans = 0
for n in range(len(S)):
  if S[n] != T[n]:
    ans += 1
print(ans)