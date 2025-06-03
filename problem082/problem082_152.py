
S, T = [input() for x in range(2)]
lenT = len(T)
max_match_len = 0

for i in range(len(S)-lenT+1):
  compareS = S[i:i+lenT]
  match_len = 0
  for j in range(lenT):
    if compareS[j] == T[j]:
      match_len += 1
  else:
    if max_match_len < match_len:
      max_match_len = match_len
print(lenT - max_match_len)
