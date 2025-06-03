class Dice:
    def __init__(self,num):
        self.num = num.copy()
        
    def east(self):
        temp = self.num.copy()
        self.num[1-1] = temp[4-1]
        self.num[4-1] = temp[6-1]
        self.num[6-1] = temp[3-1]
        self.num[3-1] = temp[1-1]

    def north(self):
        temp = self.num.copy()
        self.num[1-1] = temp[2-1]
        self.num[2-1] = temp[6-1]
        self.num[6-1] = temp[5-1]
        self.num[5-1] = temp[1-1]

    def south(self):
        temp = self.num.copy()
        self.num[1-1] = temp[5-1]
        self.num[5-1] = temp[6-1]
        self.num[6-1] = temp[2-1]
        self.num[2-1] = temp[1-1]

    def west(self):
        temp = self.num.copy()
        self.num[1-1] = temp[3-1]
        self.num[3-1] = temp[6-1]
        self.num[6-1] = temp[4-1]
        self.num[4-1] = temp[1-1]

    def right(self):
        temp = self.num.copy()
        self.num[2-1] = temp[4-1]
        self.num[4-1] = temp[5-1]
        self.num[5-1] = temp[3-1]
        self.num[3-1] = temp[2-1]

num = list(map(int,input().split()))
dice = Dice(num)
q = int(input())
for _ in range(q):
    top,front = map(int,input().split())
    while not (top == dice.num[0] or front == dice.num[1]): dice.north()
    while top != dice.num[0]: dice.east()
    while front != dice.num[1]: dice.right()
    print(dice.num[2])
        

