inputs = [int(d) for d in input().split()]

results = []
for i in (0, 1):
  for j in (2, 3):
    results.append(inputs[i] * inputs[j])

print(max(results))
