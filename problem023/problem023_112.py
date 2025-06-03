se = set([])
n = int(raw_input())
for i in range(n):
    s = raw_input().split()
    if s[0] == 'insert':
        se.add(s[1])
    elif s[0] == 'find':
        if s[1] in se:
            print 'yes'
        else:
            print 'no'