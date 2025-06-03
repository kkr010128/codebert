seed = [i for i in range(1,14)]
deck = {}
for s in ['S','H','C','D']:
    deck[s] = seed[:]

n = int(input())
for i in range(n):
    s,v = input().split()
    deck[s][int(v)-1] = 0

for s in ['S','H','C','D']:
    for i in deck[s]:
        if i != 0:
            print(s,i)