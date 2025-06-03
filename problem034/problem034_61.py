import enum
class Direction(enum.Enum):
    N = "N"
    E = "E"
    W = "W"
    S = "S"

    @classmethod
    def value_of(cls, value):
        return [v for v in cls if v.value == value][0]


class Dice:
    def __init__(self, *value_list):
        self.__value_list = list(value_list)

    def rotate(self, direction):
        l = self.__value_list
        if  direction == Direction.N:
            l[0],l[1],l[5],l[4] = l[1],l[5],l[4],l[0]
        elif  direction == Direction.E:
            l[0],l[2],l[5],l[3] = l[3],l[0],l[2],l[5]
        elif  direction == Direction.W:
            l[0],l[2],l[5],l[3] = l[2],l[5],l[3],l[0]
        elif  direction == Direction.S:
            l[0],l[1],l[5],l[4] = l[4],l[0],l[1],l[5]

    def adjust_top_front(self, top_value, front_value):
        for _ in range(2):
            for _ in range(3):
                if self.front_value() == front_value:
                    break
                self.rotate(Direction.N)
            if self.front_value() == front_value:
                break
            self.rotate(Direction.E)
        
        for _ in range(3):
            if self.top_value() == top_value:
                break
            self.rotate(Direction.E)

    def top_value(self):
        return self.__value_list[0]

    def front_value(self):
        return self.__value_list[1]

    def right_value(self):
        return self.__value_list[2]


dice = Dice(*input().split())
for _ in range(int(input())):
    top,front = input().split()
    dice.adjust_top_front(top, front)
    print(dice.right_value())
