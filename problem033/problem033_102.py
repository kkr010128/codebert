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


dice = Dice([int(i) for i in sys.stdin.readline().split()])
command = sys.stdin.readline().strip()
for c in command:
    if c == "N":
        dice.roll_north()
    elif c == "S":
        dice.roll_south()
    elif c == "W":
        dice.roll_west()
    elif c == "E":
        dice.roll_east()
print(dice.number(1))