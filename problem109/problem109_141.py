import collections
a = input()
N = int(a)
S = [input() for i in range(N)]

c = collections.Counter(S)

print('AC x %d' % c['AC'])
print('WA x %d' % c['WA'])
print('TLE x %d' % c['TLE'])
print('RE x %d' % c['RE'])