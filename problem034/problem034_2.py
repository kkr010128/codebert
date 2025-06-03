dice = list(map(int, input().split()))
q = int(input())

class Dice():
    def __init__(self, dice, top, front):
        self.dice = dice
        self.top = top
        self.front = front

    def get_right(self):
        right_list =[
            (1, 2, 4, 3), #0
            (0, 3, 5, 2), #1
            (0, 1, 5, 4), #2
            (0, 4, 5, 1), #3
            (0, 2, 5, 3), #4
            (1, 3, 4, 2)  #5
        ]

        for i in range(6):
            if self.dice[i] == self.top:
                for j in range(4):
                    if self.dice[right_list[i][j]] == self.front:
                        print(self.dice[right_list[i][j-3]])

for i in range(q):
    top, front = map(int, input().split())
    dice_right = Dice(dice, top, front)
    dice_right.get_right()
