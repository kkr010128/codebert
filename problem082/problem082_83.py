S = input()
T = input()

s = len(S)
t = len(T)
ans1 = 10000000

for i in range(s - t + 1):
  ans = 0
  for j in range(t):
    if T[j] != S[i + j]:
      ans += 1
      
  ans1 = min(ans, ans1)
      
print(ans1)
