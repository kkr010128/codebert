S = ['S', 'H', 'C', 'D']
D = map(str, range(1, 14))
n = input()
T = [tuple(raw_input().split()) for _ in xrange(n)]

for t in [(s, d) for s in S for d in D]:
    if t not in T:
        print ' '.join(t)