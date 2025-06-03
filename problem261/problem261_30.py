S = input()

S_rev = S[::-1]
total = 0

for i in range(len(S)):
  if S[i] != S_rev[i]:
    total += 1

if total % 2 == 0:
  total = int(total / 2)
else:
  total = int(total / 2) + 1

print(total)