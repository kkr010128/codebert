S = input()
length =len(S)
S = list(S)
count = 0

for i in range(length):
  if S[i] == '?':
    S[i] = 'D'

answer = "".join(S)
print(answer)