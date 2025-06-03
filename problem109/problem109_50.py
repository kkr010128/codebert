results = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
N = int(input())
for _ in range(N):
  S = input()
  results[S] = results[S] + 1

for k, v in results.items():
  print(k, 'x', v)