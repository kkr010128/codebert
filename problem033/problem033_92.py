class Dice:
    def __init__(self, labels):
        self._top = labels[0]
        self._front = labels[1]
        self._right = labels[2]
        self._left = labels[3]
        self._back = labels[4]
        self._bottom = labels[5]
    
    def top(self):
        return self._top
    
    def front(self):
        return self._front
    
    def right(self):
        return self._right
    
    def left(self):
        return self._left
    
    def back(self):
        return self._back
    
    def bottom(self):
        return self._bottom
    
    def role(self, directions):
        for d in directions:
            self._role1(d)
    
    def _role1(self, d):
        if d == "N":
            self._top, self._front, self._bottom, self._back = \
            self._front, self._bottom, self._back, self._top
        elif d == "E":
            self._top, self._left, self._bottom, self._right = \
            self._left, self._bottom, self._right, self._top
        elif d == "S":
            self._top, self._back, self._bottom, self._front = \
            self._back, self._bottom, self._front, self._top
        else:
            self._top, self._right, self._bottom, self._left = \
            self._right, self._bottom, self._left, self._top


xs = list(map(int, input().split()))
directions = input()

dice = Dice(xs)
dice.role(directions)

print(dice.top())
