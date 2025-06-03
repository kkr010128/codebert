import sys

class Dice(object):
    def __init__(self, dice):
        self.__dice = dice

    def roll_north(self):
        self.__dice = (self.__dice[1], self.__dice[5], self.__dice[2],
                       self.__dice[3], self.__dice[0], self.__dice[4])

    def roll_south(self):
        self.__dice = (self.__dice[4], self.__dice[0], self.__dice[2],
                       self.__dice[3], self.__dice[5], self.__dice[1])

    def roll_west(self):
        self.__dice = (self.__dice[2], self.__dice[1], self.__dice[5],
                       self.__dice[0], self.__dice[4], self.__dice[3])

    def roll_east(self):
        self.__dice = (self.__dice[3], self.__dice[1], self.__dice[0],
                       self.__dice[5], self.__dice[4], self.__dice[2])

    def number(self, face_id):
        return self.__dice[face_id - 1]

    def __str__(self):
        return str(self.__dice)


dice = Dice([int(i) for i in sys.stdin.readline().split()])
n = int(sys.stdin.readline())
for i in range(n):
    (face1, face2) = [int(a) for a in sys.stdin.readline().split()]
    if face2 == dice.number(3) or face2 == dice.number(4):
        dice.roll_west()
    while dice.number(2) != face2:
        dice.roll_north()
    while dice.number(1) != face1:
        dice.roll_west()
    print(dice.number(3))