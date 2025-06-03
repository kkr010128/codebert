from sys import stdin

cards = {}

n = int(input())
for line in stdin:
    m, num = line.rstrip().split(' ')
    cards[(m, int(num))] = True

for s in ['S','H','C','D']:
    for i in range(1, 14):
        if not (s, i) in cards:
            print("{} {}".format(s, i))