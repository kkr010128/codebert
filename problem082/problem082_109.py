S, T = [input() for x in range(2)]
max_match_len = 0

for i in range(len(S)):
  if len(S) - len(T) < i:
    break
  compare_s = S[i:i+len(T)]
  match_len = 0
  for j in range(len(T)):
    if compare_s[j] == T[j]:
      match_len += 1
  else:
    if max_match_len < match_len:
      max_match_len = match_len
print(len(T) - max_match_len)