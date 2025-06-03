class Reader:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.buf = [0 for _ in range(c+1)]

    def __call__(self, s):
        total = 0
        for i, v in enumerate(map(int, s.split())):
            self.buf[i] += v
            total += v
        self.buf[-1] += total
        return " ".join((s, str(total)))

    def __str__(self):
        return " ".join(map(str, self.buf))

r, c = list(map(int, input().split()))
reader = Reader(r, c)

for _ in range(r):
    print(reader(input()))
print(reader)