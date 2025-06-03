list_data = [input() for _ in range(2)]

s = list_data[0]
t = list_data[1]

len_t = len(t)

max_correct = 0
for i in range(len(s)-len(t)+1):
  correct = 0
  for j in range(len(t)):
    if s[i+j] == t[j]:
      correct += 1
  
  if max_correct < correct:
    max_correct = correct

print(len_t - max_correct)