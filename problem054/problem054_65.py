deck = [(s, n) for s in ['S', 'H', 'C', 'D'] for n in range(1,  14)]
N = input()
for n in range(N):
    s, n = raw_input().split()
    deck.remove((s, int(n)))

for s, n in deck:
    print s, n