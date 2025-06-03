# 10_*
class Dice:
    def __init__(self, label: list):
        self.top, self.front, self.right, self.left, self.back, self.bottom = label

    def roll(self, direction: str):
        if direction == "N":
            self.top, self.front, self.right, self.left, self.back, self.bottom = (
                self.front,
                self.bottom,
                self.right,
                self.left,
                self.top,
                self.back,
            )
        elif direction == "W":
            self.top, self.front, self.right, self.left, self.back, self.bottom = (
                self.right,
                self.front,
                self.bottom,
                self.top,
                self.back,
                self.left,
            )
        elif direction == "S":
            self.top, self.front, self.right, self.left, self.back, self.bottom = (
                self.back,
                self.top,
                self.right,
                self.left,
                self.bottom,
                self.front,
            )
        elif direction == "E":
            self.top, self.front, self.right, self.left, self.back, self.bottom = (
                self.left,
                self.front,
                self.top,
                self.bottom,
                self.back,
                self.right,
            )

    def output_top(self):
        print(self.top)

    def get_top_front(self):
        return f"{self.top} {self.front}"

    def print_right(self):
        print(self.right)


# 10_A
# (*label,) = map(int, input().split())
# dice = Dice(label)
# for i in input():
#     dice.roll(i)
# dice.output_top()

# 10_B
(*label,) = map(int, input().split())
dice = Dice(label)
q = int(input())
for _ in range(q):
    t, f = map(int, input().split())
    for i in "EEEN" * 2 + "EEES" * 2 + "EEEN" * 2:
        if f"{t} {f}" == dice.get_top_front():
            dice.print_right()
            break
        dice.roll(i)
