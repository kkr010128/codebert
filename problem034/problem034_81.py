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
            
first_state = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    my_dice = Dice(first_state)
    a, b = map(int, input().split())

    if b == my_dice.spots[0]:
        my_dice.roll(2)
    elif b == my_dice.spots[1]:
        pass
    elif b == my_dice.spots[2]:
        my_dice.roll(3)
        my_dice.roll(2)
    elif b == my_dice.spots[3]:
        my_dice.roll(1)
        my_dice.roll(2)
    elif b == my_dice.spots[4]:
        my_dice.roll(2)
        my_dice.roll(2)
    elif b == my_dice.spots[5]:
        my_dice.roll(0)
    
    if a == my_dice.spots[0]:
        pass
    elif a == my_dice.spots[2]:
        my_dice.roll(3)
    elif a == my_dice.spots[3]:
        my_dice.roll(1)
    elif a == my_dice.spots[5]:
        my_dice.roll(1)
        my_dice.roll(1)
        
    print(my_dice.spots[2])
        
