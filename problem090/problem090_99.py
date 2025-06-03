from sys import stdin


test = list(stdin.readline().rstrip())

count = [0,0,0]
i=0
before = 'R'

for str in test:
    if str=='R':
        count[i] += 1
    else:
        i = i + 1

print(max(count))
