N = int(input())
count = {}
max_count = 0
for _ in range(N):
  s = input()
  if s not in count:
    count[s] = 0
  count[s] += 1
  max_count = max(max_count, count[s])

longest = []
for s, c in count.items():
  if c == max_count:
    longest.append(s)

longest.sort()
for s in longest:
  print(s)