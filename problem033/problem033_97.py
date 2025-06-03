class Dice(object):
    """Dice Class

    """

    def __init__(self, numbers):
        """

        Args:
            numbers:
        """
        self.numbers = {1: numbers[0], 2: numbers[1], 3: numbers[2], 4: numbers[3], 5: numbers[4], 6: numbers[5]}

        self.vertical = [self.numbers[1], self.numbers[2], self.numbers[6], self.numbers[5]]
        self.horizontal = [self.numbers[4], self.numbers[1], self.numbers[3], self.numbers[6]]

    def move_dice(self, s):
        """

        Args:
            s: move direction

        Returns:

        """
        if s == 'N':
            self.move_north()
        elif s == 'S':
            self.move_south()
        elif s == 'W':
            self.move_west()
        elif s == 'E':
            self.move_east()

    def move_south(self):
        """move this dice towered north
        """
        self.vertical = (self.vertical * 2)[3:7]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]

    def move_north(self):
        """move this dice towered south
        """
        self.vertical = (self.vertical * 2)[1:5]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]

    def move_east(self):
        """move this dice towered east
        """
        self.horizontal = (self.horizontal * 2)[3:7]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]

    def move_west(self):
        """move this dice towered west
        """
        self.horizontal = (self.horizontal * 2)[1:5]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]

    def get_top(self):
        return self.vertical[0]


numbers = [int(x) for x in raw_input().split()]
dice1 = Dice(numbers=numbers)
for s in raw_input():
    dice1.move_dice(s)

print(dice1.get_top())