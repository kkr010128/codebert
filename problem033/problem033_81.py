class dice:
    def __init__(self, X):
        self.x = [0] * 6
        self.x[0] = X[0]
        self.x[1] = X[1]
        self.x[2] = X[2]
        self.x[3] = X[3]
        self.x[4] = X[4]
        self.x[5] = X[5]

    def roll(self, d):
        if d == 'S':
            self.x[0], self.x[1], self.x[2], self.x[3], self.x[4], self.x[5] = \
            self.x[4], self.x[0], self.x[2], self.x[3], self.x[5], self.x[1]
        elif d == 'E':
            self.x[0], self.x[1], self.x[2], self.x[3], self.x[4], self.x[5] = \
            self.x[3], self.x[1], self.x[0], self.x[5], self.x[4], self.x[2]
        elif d == 'W':
            self.x[0], self.x[1], self.x[2], self.x[3], self.x[4], self.x[5] = \
            self.x[2], self.x[1], self.x[5], self.x[0], self.x[4], self.x[3]
        elif d == 'N':
            self.x[0], self.x[1], self.x[2], self.x[3], self.x[4], self.x[5] = \
            self.x[1], self.x[5], self.x[2], self.x[3], self.x[0], self.x[4]

X = list(map(int, input().split()))
directions = list(input())
d_one = dice(X)
for dist in directions:
    d_one.roll(dist)
print(d_one.x[0])
