house = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
for i in range(int(input())):
    b, f, r, v = map(int, input().split())
    house[b-1][f-1][r-1] += v
for b in range(4):
    for f in range(3):
        house[b][f] = ' ' + ' '.join(map(str, house[b][f]))
    house[b] = '\n'.join(map(str, house[b])) + '\n'
border = '#' * 20 + '\n'
house = border.join(map(str, house))
print(house.rstrip())