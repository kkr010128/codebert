n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input().rstrip()
d1 = {'r': ('p', p), 's': ('r', r), 'p': ('s', s)}
d2 = {'r': {'p': 'r', 's': 's', 'r': 's'},
      's': {'r': 's', 'p': 'p', 's': 's'},
      'p': {'r': 'r', 's': 'p', 'p': 'r'}}
ret = 0
me = []
for i, rival in enumerate(t):
    if i - k < 0 or me[i - k] != d1[rival][0]:
        me.append(d1[rival][0])
        ret += d1[rival][1]
    elif i - k >= 0 and me[i - k] == d1[rival][0] and i + k < n:
        me.append(d2[rival][t[i + k]])
print(ret)
