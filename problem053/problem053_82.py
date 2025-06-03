p = input()
n = raw_input().split()
n.reverse()
s = ''
for i in xrange(len(n) - 1):
    s += n[i] + ' '
s += n[len(n) - 1]
print s