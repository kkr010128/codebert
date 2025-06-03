class dice():
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
q = int(input())
dice1 = dice()

for i in range(q):
    top, flont = map(int, input().split())
    if num1[dice1.flont-1] == flont and num1[dice1.top-1] == top:
        ans = num1[dice1.right-1]
    for j in range(4):
        for k in range(4):
            dice1.do_E()
            if num1[dice1.flont-1] == flont and num1[dice1.top-1] == top:
                ans = num1[dice1.right-1]
        dice1.do_N()
        if num1[dice1.flont-1] == flont and num1[dice1.top-1] == top:
            ans = num1[dice1.right-1]

    dice1.do_S()
    dice1.do_E()
    if num1[dice1.flont-1] == flont and num1[dice1.top-1] == top:
        ans = num1[dice1.right-1]
    for j in range(4):
        for k in range(4):
            dice1.do_E()
            if num1[dice1.flont-1] == flont and num1[dice1.top-1] == top:
                ans = num1[dice1.right-1]
        dice1.do_N()
        if num1[dice1.flont-1] == flont and num1[dice1.top-1] == top:
            ans = num1[dice1.right-1]


    print(str(ans))
