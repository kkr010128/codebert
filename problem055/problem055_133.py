class Residents:

    def __init__(self):
        self.official_house = []

        for b in range(4):
            self.official_house.append([])
            for f in range(3):
                self.official_house[b].append([])
                for r in range(10):
                    self.official_house[b][f].append(0)

    def move_in(self, building, floor, room, num):
        building -= 1
        floor -= 1
        room -= 1
        if self.official_house[building][floor][room] + num > 9:
            self.official_house[building][floor][room] = 9 
        else:
            self.official_house[building][floor][room] += num 

    def move_out(self, building, floor, room, num):
        building -= 1
        floor -= 1
        room -= 1
        if self.official_house[building][floor][room] < num:
            self.official_house[building][floor][room] = 0 
        else:
            self.official_house[building][floor][room] -= num 

    def show(self, building, floor, room):
        building -= 1
        floor -= 1
        room -= 1
        return self.official_house[building][floor][room]

    def output(self):
        result = ''
        for b in range(4):
            if b > 0:
                result += '#' * 20 + '\n'
            for f in range(3):
                for r in range(10):
                    result += ' ' + str(self.official_house[b][f][r])
                result += '\n'

        return result

if __name__ == '__main__':

    residents = Residents()
    rows = int(input())

    for i in range(rows):
        (b, f, r, num) = [int(i) for i in input().split(' ')]
        if num > 0:
            residents.move_in(b, f, r, num)
        else:
            residents.move_out(b, f, r, num * -1)

    print(residents.output(), end='')