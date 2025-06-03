S = input()
T = input()
ans = len(T)
for i in range(len(S)-len(T)+1):
  count = 0
  #print(S[i:i+len(T)], T)
  for s, t in zip(S[i:i+len(T)], T):
    if s != t:
      count += 1
  ans = min(count, ans)
print(ans)