S = input()
T = input()
list_s = []
list_t = []
counter = 0
for i in range(0, len(S)):
  list_s.append(S[i])
  list_t.append(T[i])
  if S[i] != T[i]:
    list_s[i] = list_t[i]
    counter += 1
print(counter)