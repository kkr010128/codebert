import collections
n, m = map(int, input().split())
linked = collections.defaultdict(list)
i2group = dict()

gid = n + 1
def get_root(i):
  if i not in linked:
    return i
  j = get_root(linked[i])
  linked[i] = j
  return j

def get_groups():
  return [get_root(i) for i in range(1, n + 1)]

for i in range(m):
  a, b = map(int, input().split())
  ra, rb = get_root(a), get_root(b)
  if ra == rb: continue
  linked[ra] = gid
  linked[rb] = gid
  gid += 1

g = get_groups()
print(len(set(g)) - 1)
exit()

n_connected = 0
n_group = 0
for s in linked.values():
  s = s[0]
  if s:
    n_group += 1
    n_connected += len(s)
    s.clear()
print((n - n_connected) + (n_group - 1))
