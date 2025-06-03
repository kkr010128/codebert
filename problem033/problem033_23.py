class Dice:
    def __init__(self, eye1, eye2, eye3, eye4, eye5, eye6):
        self.eye1 = eye1
        self.eye2 = eye2
        self.eye3 = eye3
        self.eye4 = eye4
        self.eye5 = eye5
        self.eye6 = eye6
    
    def N(self):
        self.eye1, self.eye2, self.eye6, self.eye5 = self.eye2, self.eye6, self.eye5, self.eye1
    def S(self):
        self.eye2, self.eye6, self.eye5, self.eye1 = self.eye1, self.eye2, self.eye6, self.eye5
    def E(self):
        self.eye1, self.eye3, self.eye6, self.eye4 = self.eye4, self.eye1, self.eye3, self.eye6
    def W(self):
        self.eye4, self.eye1, self.eye3, self.eye6 = self.eye1, self.eye3, self.eye6, self.eye4
    
    def print_top(self):
        print(self.eye1)


eye1, eye2, eye3, eye4, eye5, eye6 = map(int, input().split())
commands = input()
dice1 = Dice(eye1, eye2, eye3, eye4, eye5, eye6)
for command in commands:
    if command == 'N':
        dice1.N()
    elif command == 'S':
        dice1.S()
    elif command == 'E':
        dice1.E()
    else:
        dice1.W()

dice1.print_top()
