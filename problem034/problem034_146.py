num = list(map(int, input().split()))
class Dice:
    def __init__(self, num):
        self.state = {}
        for i in range(1,6+1):
            self.state[i] = num[i-1]

        self.reversed_state = {}
        for key,val in zip(self.state.keys(), self.state.values()):
            self.reversed_state[val] = key
        
    def search_side(self, x,y):
        a = self.reversed_state[x]
        b = self.reversed_state[y]
        if str(a)+str(b) in '12651':
            side = self.state[3]
        elif str(b)+str(a) in '12651':
            side = self.state[4]
        elif str(a)+str(b) in '13641':
            side = self.state[5]
        elif str(b)+str(a) in '13641':
            side = self.state[2]
        elif str(a)+str(b) in '23542':
            side = self.state[1]
        elif str(b)+str(a) in '23542':
            side = self.state[6]
        return side
        
dice = Dice(num)
q = int(input())
for _ in range(q):
    x,y = map(int, input().split())
    ans = dice.search_side(x,y)
    print(ans)
