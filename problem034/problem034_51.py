class Dice:
    def __init__(self,numbers):
        self.surface=numbers

    def find_right_side(self,top,flont):
        tf=str(self.surface.index(top))+str(self.surface.index(flont))
        if tf in '12431':
            return int(self.surface[0])
        elif tf in '03520':
            return int(self.surface[1])
        elif tf in '01540':
            return int(self.surface[2])
        elif tf in '04510':
            return int(self.surface[3])
        elif tf in '02530':
            return int(self.surface[4])
        else:
            return int(self.surface[5])

dice=Dice(input().split())
q=int(input())
for i in range(q):
    top,flont=input().split()
    print(dice.find_right_side(top,flont))
