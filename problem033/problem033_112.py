class dice():
    def __init__(self, num_list):
        self.dice_index = 0
        i = self.dice_index
        self.NS = [num_list[i], num_list[i+1], num_list[i+5], num_list[i+4]]
        self.WE = [num_list[i], num_list[i+2], num_list[i+5], num_list[i+3]]

    def set_dict(self, direction):
        i = self.dice_index
        if direction == 'N' or direction == 'W':
            m = 1
        elif direction == 'S' or direction == 'E':
            m = -1
        if direction == 'N' or direction == 'S':
            self.dice_index = self.NS[m]
            self.NS = self.NS[m:]+self.NS[:m]
            self.WE[0] = self.NS[0]
            self.WE[2] = self.NS[2]
        elif direction == 'W' or direction == 'E':
            self.dice_index = self.WE[m]
            self.WE = self.WE[m:]+self.WE[:m]
            self.NS[0] = self.WE[0]
            self.NS[2] = self.WE[2]


if __name__ == '__main__':
    dice_number = input()
    dice_direction = input()
    dice_number = dice_number.split()
    Dice = dice(dice_number)
    for i in range(len(dice_direction)):
        Dice.set_dict(dice_direction[i])
    else:
        print(Dice.dice_index)

