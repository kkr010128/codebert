string1 = input()
string2 = input()

n, m = len(string1), len(string2)
best = float("inf")
for i in range(n - m + 1):
  current = string1[i:i+m]
  differences = 0
  for i in range(m):
    if current[i] != string2[i]:
      differences += 1
  best = min(differences, best)

if best == float("inf"):
  print(0)
else:
  print(best)