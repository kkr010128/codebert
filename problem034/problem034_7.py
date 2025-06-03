class Dice():
    def __init__(self, dice_labels):
        self.top = dice_labels[0]
        self.south = dice_labels[1]
        self.east = dice_labels[2]
        self.west = dice_labels[3]
        self.north = dice_labels[4]
        self.bottom = dice_labels[5]

    def roll(self, str_direction):
        if str_direction == 'E':
            self.__roll_to_east()
        elif str_direction == 'W':
            self.__roll_to_west()
        elif str_direction == 'S':
            self.__roll_to_south()
        elif str_direction == 'N':
            self.__roll_to_north()

    def turn(self, str_direction):
        if str_direction == 'L':
            self.__turn_left()
        elif str_direction == 'R':
            self.__turn_right()

    def __roll_to_east(self):
        self.top, self.east, self.west, self.bottom = (self.west, self.top, self.bottom, self.east)

    def __roll_to_west(self):
        self.top, self.east, self.west, self.bottom = (self.east, self.bottom, self.top, self.west)

    def __roll_to_south(self):
        self.top, self.south, self.north, self.bottom = (self.north, self.top, self.bottom, self.south)

    def __roll_to_north(self):
        self.top, self.south, self.north, self.bottom = (self.south, self.bottom, self.top, self.north)

    def __turn_right(self):
        self.south, self.east, self.west, self.north = (self.east, self.north, self.south, self.west)

    def __turn_left(self):
        self.south, self.east, self.west, self.north = (self.west, self.south, self.north, self.east)

dice_labels = input().split(' ')
num_question = int(input())
dice = Dice(dice_labels)

for i in range(0, num_question):
    target_top_label, target_for_label = tuple(input().split(' '))
    for j in range(0, 2):
        for k in range(0, 4):
            if dice.top != target_top_label:
                dice.roll('N')
        dice.turn('R')

    for j in range(0, 4):
        if dice.south != target_for_label:
            dice.turn('R')

    print(dice.east)
