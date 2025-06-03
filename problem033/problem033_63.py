class Dice:
    def __init__(self, hoge):
        self.num = hoge
        self.face = {'U': 0, 'W': 3, 'E': 2, 'N': 4, 'S': 1, 'B': 5} 
    
    def move(self, direct):
        previouse = {k: v for k, v in self.face.items()}
        if direct == 'E':
            self.face['U'] = previouse['W']
            self.face['W'] = previouse['B']
            self.face['E'] = previouse['U']
            self.face['B'] = previouse['E']
        elif direct == 'W':
            self.face['U'] = previouse['E']
            self.face['W'] = previouse['U']
            self.face['E'] = previouse['B']
            self.face['B'] = previouse['W']
        elif direct == 'N':
            self.face['U'] = previouse['S']
            self.face['N'] = previouse['U']
            self.face['S'] = previouse['B']
            self.face['B'] = previouse['N']
        elif direct == 'S':
            self.face['U'] = previouse['N']
            self.face['N'] = previouse['B']
            self.face['S'] = previouse['U']
            self.face['B'] = previouse['S']
    
    def get_upper(self):
        return self.num[self.face['U']]
        
if __name__ == '__main__':
    dice = Dice([int(x) for x in input().split()])
    for d in input():
        dice.move(d)
    print (dice.get_upper())
