class Dice:
    
    def __init__(self, U, S, E, W, N, D):
        self.u, self.d = U, D
        self.e, self.w = E, W
        self.s, self.n = S, N       
    
    def roll(self, commmand):
        if command == 'E':
            self.e, self.u, self.w, self.d = self.u, self.w, self.d, self.e
        elif command == 'W':
            self.e, self.u, self.w, self.d = self.d, self.e, self.u, self.w
        elif command == 'S':
            self.s, self.u, self.n, self.d = self.u, self.n, self.d, self.s
        else:
            self.s, self.u, self.n, self.d = self.d, self.s, self.u, self.n

    def rightside(self, upside, forward):
        self.structure = {self.u:{self.w: self.s, self.s: self.e, self.e: self.n, self.n: self.w},
                          self.d:{self.n: self.e, self.e: self.s, self.s: self.w, self.w: self.n},
                          self.e:{self.u: self.s, self.s: self.d, self.d: self.n, self.n: self.u},
                          self.s:{self.u: self.w, self.w: self.d, self.d: self.e, self.e: self.u},
                          self.w:{self.u: self.n, self.n: self.d, self.d: self.s, self.s: self.u},
                          self.n:{self.u: self.e, self.e: self.d, self.d: self.w, self.w: self.u}}
        
        print(self.structure[upside][forward])

U, S, E, W, N, D = [int(i) for i in input().split()]
turns = int(input())
dice1 = Dice(U, S, E, W, N, D)
for i in range(turns):
    upside, forward = [int(k) for k in input().split()]
    dice1.rightside(upside, forward)
