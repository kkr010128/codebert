S = input()
T = input()
l = len(S) - len(T) + 1
ans = len(T)
t = len(T)
for i in range(l):
  s = S[i:i+t]
  ans = min(ans, len([0 for i in range(t) if T[i] != s[i]]))
print(ans)