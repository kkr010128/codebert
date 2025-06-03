class Dice():
    def __init__(self, spots):
        self.spots = [spots[i] for i in range(6)]
    
    def roll(self, direction):
        if direction == 0:
            self.spots = [self.spots[i] for i in [1, 5, 2, 3, 0, 4]]
        elif direction == 1:
            self.spots = [self.spots[i] for i in [3, 1, 0, 5, 4, 2]]
        elif direction == 2:
            self.spots = [self.spots[i] for i in [4, 0, 2, 3, 5, 1]]
        elif direction == 3:
            self.spots = [self.spots[i] for i in [2, 1, 5, 0, 4, 3]]
            
    
spots = list(map(int, input().split()))
moves = input()
my_dice = Dice(spots=spots)
for move in moves:
    if move == 'N':
        my_dice.roll(0)
    elif move == 'E':
        my_dice.roll(1)
    elif move == 'S':
        my_dice.roll(2)
    elif move == 'W':
        my_dice.roll(3)
        
print(my_dice.spots[0])
        
