ret = []
while True:
    m, f, r = map(int, raw_input().split())
    if (m,f,r) == (-1, -1, -1):
        break
    if m == -1 or f == -1:
        ret += 'F'
    elif 80 <= m + f:
        ret += ['A']
    elif 65 <= m + f < 80:
        ret += ['B']
    elif 50 <= m + f < 65:
        ret += ['C']
    elif 30 <= m + f < 50 and 50 <= r:
        ret += ['C']
    elif 30 <= m + f < 50 and r < 50:
        ret += ['D']
    elif m + f < 30:
        ret += ['F']

for i in ret:
    print i