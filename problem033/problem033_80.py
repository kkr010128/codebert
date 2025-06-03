class Dice:
    def __init__(self, usr_input, command):
        self.eyes = list(map(int, usr_input.split()))
        self.pos = {label:eye for label, eye in zip(range(1, 7), self.eyes)}
        self.com = list(command)

    def roll(self):
        for c in self.com:
            self.eyes = [n for n in self.pos.values()]
            if c == 'E':
                self.pos[1] = self.eyes[3]
                self.pos[3] = self.eyes[0]
                self.pos[4] = self.eyes[5]
                self.pos[6] = self.eyes[2]
            elif c == 'N':
                self.pos[1] = self.eyes[1]
                self.pos[2] = self.eyes[5]
                self.pos[5] = self.eyes[0]
                self.pos[6] = self.eyes[4]
            elif c == 'S':
                self.pos[1] = self.eyes[4]
                self.pos[2] = self.eyes[0]
                self.pos[5] = self.eyes[5]
                self.pos[6] = self.eyes[1]
            elif c == 'W':
                self.pos[1] = self.eyes[2]
                self.pos[3] = self.eyes[5]
                self.pos[4] = self.eyes[0]
                self.pos[6] = self.eyes[3]

    def top_print(self):
        print(self.pos.get(1))

if __name__ == '__main__':
    dice1 = Dice(input(), input())
    dice1.roll()
    dice1.top_print()