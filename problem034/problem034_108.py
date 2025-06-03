class Dice():
    def __init__(self, a, b, c, d, e, f):
        """面の数字とindexを一致させるために0を挿入"""
        self.s = [0, a, b, c, d, e, f]

    def rotate(self, dir):
        if dir == "N":
            self.s[0] = self.s[1] #s[0]に一時的にs[1]を保持
            self.s[1] = self.s[2] 
            self.s[2] = self.s[6]
            self.s[6] = self.s[5]
            self.s[5] = self.s[0]
            return

        elif dir == "W":
            self.s[0] = self.s[1]
            self.s[1] = self.s[3] 
            self.s[3] = self.s[6]
            self.s[6] = self.s[4]
            self.s[4] = self.s[0]
            return

        elif dir == "S":
            self.s[0] = self.s[1]
            self.s[1] = self.s[5] 
            self.s[5] = self.s[6]
            self.s[6] = self.s[2]
            self.s[2] = self.s[0]
            return

        elif dir == "E":
            self.s[0] = self.s[1]
            self.s[1] = self.s[4] 
            self.s[4] = self.s[6]
            self.s[6] = self.s[3]
            self.s[3] = self.s[0]
            return
        
        elif dir == "R":
            self.s[0] = self.s[2]
            self.s[2] = self.s[3] 
            self.s[3] = self.s[5]
            self.s[5] = self.s[4]
            self.s[4] = self.s[0]
            return

        elif dir == "L":
            self.s[0] = self.s[2]
            self.s[2] = self.s[4] 
            self.s[4] = self.s[5]
            self.s[5] = self.s[3]
            self.s[3] = self.s[0]
            return

        else:
            return


dice = Dice(*list(map(int, input().split())))

for _ in range(int(input())):
    t, s = map(int, input().split())

    while dice.s[1] != t:
        dice.rotate("S")
        if dice.s[1] != t:
            dice.rotate("E")
    
    while dice.s[2] != s:
        dice.rotate("R")

    print(dice.s[3])
