N = int(input())
S = [input() for n in range(N)]
assert len(S) == N
counts = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}

for s in S:
  counts[s] += 1

for key in ['AC', 'WA', 'TLE', 'RE']:
	print('{} x {}'.format(key, counts[key]))