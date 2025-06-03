s = input()
map = {'SSS': 0, 'SSR': 1, 'SRS': 1, 'RSS': 1, 'SRR': 2, 'RSR': 1, 'RRS': 2, 'RRR': 3}
for key in map.keys():
    if s == key:
        print(map[key])
        break