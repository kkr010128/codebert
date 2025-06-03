class Dice:
    def __init__(self):
        self.N = [1, 5, 2, 3, 0, 4]
        self.S = [4, 0, 2, 3, 5, 1]
        self.E = [3, 1, 0, 5, 4, 2]
        self.W = [2, 1, 5, 0, 4, 3]
    
    def roll(self, dice, dice_t, direction):
        for d in direction:
            if d == "N":
                for i in range(6):
                    dice_t[i] = dice[self.N[i]]
            elif d == "S":
                for i in range(6):
                    dice_t[i] = dice[self.S[i]]
            elif d == "E":
                for i in range(6):
                    dice_t[i] = dice[self.E[i]]
            else:
                for i in range(6):
                    dice_t[i] = dice[self.W[i]]
            for i in range(6):
                dice[i] = dice_t[i]

d = Dice()
dice = [dice for dice in input().split()]
dice_t = ["" for dice_t in range(6)]
direction = input()
d.roll(dice, dice_t, direction)
print(dice[0])