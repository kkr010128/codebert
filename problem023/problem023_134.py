n = int(raw_input().strip())
commands = []
for i in range(n):
    commands.append(raw_input().strip())


d = [False]*67108870

def hash(s):
    ret = 0
    i = 0
    for dg in s:
        if dg == 'A':
            ret += 0 * 4**i
        elif dg == 'C':
            ret += 1 * 4**i
        elif dg == 'G':
            ret += 2 * 4**i
        elif dg == 'T':
            ret += 3 * 4**i
        i += 1
    return ret

def insert(d,s):
    h = hash(s)
    d[h] = True

def find(d,s):
    h = hash(s)
    if d[h]: print 'yes'
    else: print 'no'

for c in commands:
    c += 'C'
    if c[0] == 'i':
        insert(d,c[7:])
    else:
        find(d,c[5:])