cards = {
    'S':[r for r in range(1,13+1)],
    'H':[r for r in range(1,13+1)],
    'C':[r for r in range(1,13+1)],
    'D':[r for r in range(1,13+1)]
}

n = int(input())
for nc in range(n):
    (s,r) = input().split()
    index = cards[s].index(int(r))
    del cards[s][index]

for s in ['S','H','C','D']:
    for r in cards[s]:
            print(s,r)