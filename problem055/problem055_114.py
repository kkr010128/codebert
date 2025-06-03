class Building(object):
    def __init__(self):
        self.floor = []
        self.floor.extend([[0] * 10])
        self.floor.extend([[0] * 10])
        self.floor.extend([[0] * 10])

    def change_resident(self, f, r, v):
        self.floor[f][r] += v

    def print_status(self):
        for f in self.floor:
            print(' {0}'.format(' '.join(map(str, f))))

if __name__ == '__main__':
    # ?????????4?£??????????
    buildings = []
    for i in range(4):
        buildings.append(Building())

    # ??????????????\???
    data_num = int(input())
    data = []
    for i in range(data_num):
        data.append([int(x) for x in input().split(' ')])

    # ??\?±?????????´??°
    for d in data:
        b = d[0]
        f = d[1]
        r = d[2]
        v = d[3]
        buildings[b-1].change_resident(f-1, r-1, v)

    # ?????????????????¨???
    buildings[0].print_status()
    print('#' * 20)
    buildings[1].print_status()
    print('#' * 20)
    buildings[2].print_status()
    print('#' * 20)
    buildings[3].print_status()