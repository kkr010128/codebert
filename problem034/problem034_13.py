n = [int(i) for i in input().split()]
count = int(input())
num = []

class Dice(object):
    def __init__(self,num):
        self.one = num[0]
        self.two = num[1]
        self.three = num[2]
        self.four = num[3]
        self.five = num[4]
        self.six = num[5]

    def right(self,top,forward):
        if top == self.one:
            if forward == self.two:
                return self.three
            elif forward == self.three:
                return self.five
            elif forward == self.five:
                return self.four
            elif forward == self.four:
                return self.two
        elif top == self.two:
            if forward == self.six:
                return self.three
            elif forward == self.three:
                return self.one
            elif forward == self.one:
                return self.four
            elif forward == self.four:
                return self.six
        elif top == self.three:
            if forward == self.two:
                return self.six
            elif forward == self.six:
                return self.five
            elif forward == self.five:
                return self.one
            elif forward == self.one:
                return self.two
        elif top == self.four:
            if forward == self.two:
                return self.one
            elif forward == self.one:
                return self.five
            elif forward == self.five:
                return self.six
            elif forward == self.six:
                return self.two
        elif top == self.five:
            if forward == self.one:
                return self.three
            elif forward == self.three:
                return self.six
            elif forward == self.six:
                return self.four
            elif forward == self.four:
                return self.one
        elif top == self.six:
            if forward == self.two:
                return self.four
            elif forward == self.four:
                return self.five
            elif forward == self.five:
                return self.three
            elif forward == self.three:
                return self.two


dice = Dice(n)
for i in range(count):
    num.append([int(i) for i in input().split()])

for i in range(count):
    print(dice.right(num[i][0],num[i][1]))