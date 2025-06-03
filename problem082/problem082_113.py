S = input()
T = input()
min_change = 10**9
for posi_1 in range(len(S)-len(T)+1):
  tmp = 0
  for posi_2 in range(len(T)):
    if S[posi_1+posi_2] != T[posi_2]:
      tmp += 1
  min_change = min(tmp, min_change)
print(min_change)