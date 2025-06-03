class dice:
    top = 1
    flont = 2
    right = 3
    def do_N(self):
        temp = self.flont
        self.flont = 7-self.top
        self.top = temp

    def do_S(self):
        temp = 7-self.flont
        self.flont = self.top
        self.top = temp

    def do_E(self):
        temp = self.top
        self.top = 7-self.right
        self.right = temp

    def do_W(self):
        temp = 7-self.top
        self.top = self.right
        self.right = temp

num1 = list(map(int, input().split()))
order1 = input()

dice1 = dice()
for i in range(len(order1)):
    if order1[i] == "N":
        dice1.do_N()
    elif order1[i] == "S":
        dice1.do_S()
    elif order1[i] == "E":
        dice1.do_E()
    elif order1[i] == "W":
        dice1.do_W()

print(str(num1[dice1.top-1]))
