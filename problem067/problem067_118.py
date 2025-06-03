class Reader:
    def __init__(self):
        self.l = 0
        self.r = 0

    def __call__(self, s):
        l, r = s.split()
        if l > r:
            self.l += 3
        elif l < r:
            self.r += 3
        else:
            self.l += 1
            self.r += 1

    def __str__(self):
        return "{} {}".format(self.l, self.r)

reader = Reader()

n = int(input())
for _ in range(n):
    reader(input())
print(reader)