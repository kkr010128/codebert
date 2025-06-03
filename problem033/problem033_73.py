class Dice:

    def __init__(self):
        d = map(int, raw_input().split(" "))
        self.c = raw_input()
        self.rows = [d[0], d[4], d[5], d[1]]
        self.cols = [d[0], d[2], d[5], d[3]]

    def __move_next(self, x, y):
        temp = y.pop(0)
        y.append(temp)
        x[0] = y[0]
        x[2] = y[2]

    def __move_prev(self, x, y):
        temp = y.pop(3)
        y.insert(0, temp)
        x[0] = y[0]
        x[2] = y[2]

    def execute(self):
        for i in self.c:
            self.__move(i, self.rows, self.cols)

    def __move(self, com, x, y):
        if com == "N":
            self.__move_prev(y, x)
        elif com == "S":
            self.__move_next(y, x)
        elif com == "E":
            self.__move_prev(x, y)
        elif com == "W":
            self.__move_next(x, y)

    def print_top(self):
        print self.rows[0]

dice = Dice()
dice.execute()
dice.print_top()