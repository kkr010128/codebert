S = str(input())
T = str(input())

s, t = len(S), len(T)
diff = [0 for i in range(s-t+1)]
for i in range(s-t+1):
  target = S[i:i+t]
  for j in range(t):
    if target[j] != T[j]:
      diff[i] += 1
  j = 0
print(min(diff))