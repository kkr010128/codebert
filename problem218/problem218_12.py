import collections
n = int(input())
s = [input() for l in range(n)]
word = collections.Counter(s)
ma = max(word.values())
z = [kv for kv in word.items() if kv[1] == ma]
z = sorted(z)
for c in z:
  print(c[0])
