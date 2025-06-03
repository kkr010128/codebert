a, b, c, d, e, f = map(int, input().split())
directions = [x for x in input()]


class Dice():
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def rotation(self, directions):
        for direction in directions:
            if direction == 'N':
                self.a, self.b, self.f, self.e = self.b, self.f, self.e, self.a
            if direction == 'S':
                self.a, self.b, self.f, self.e = self.e, self.a, self.b, self.f
            if direction == 'E':
                self.a, self.c, self.f, self.d = self.d, self.a, self.c, self.f
            if direction == 'W':
                self.a, self.c, self.f, self.d = self.c, self.f, self.d, self.a
        return self


dice = Dice(a, b, c, d, e, f)
print(dice.rotation(directions).a)

