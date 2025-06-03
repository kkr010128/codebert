from collections import defaultdict

n = int(input())
results = defaultdict(lambda: 0)

for _ in range(n):
  s = input()
  results[s] += 1

for judge in ['AC', 'WA', 'TLE', 'RE']:
  print(judge, ' x ', results[judge])
