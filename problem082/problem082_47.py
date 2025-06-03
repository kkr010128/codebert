S = list(input())
T = list(input())
diff = len(S)-len(T)

count, best = 0, 0

for i in range(diff+1):
  
  s = S[i:]
  
  #print('s')
  #print(s)
  
  count = 0
  for j,k in zip(s,T):
    if j == k:
      count += 1
    if count > best:
      best = count

print(len(T)-best)