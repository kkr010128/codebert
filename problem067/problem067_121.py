class Human:
    def __init__(self, name, card = "", point = 0):
        self.name = name
        self.card = card
        self.point = point
    
    def add_point(self, opponent):
        if self.card > opponent:
            self.point += 3
        elif self.card == opponent:
            self.point += 1
        else:
            pass

Taro = Human('Taro')
Hanako = Human('Hanako')

N = int(input())
for n in range(N):
    Taro.card, Hanako.card = input().split()
    Taro.add_point(Hanako.card)
    Hanako.add_point(Taro.card)

print(Taro.point, Hanako.point)
