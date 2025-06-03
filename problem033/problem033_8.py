class Dice:
    def __init__(self):
        self.side = {"top": 0, "front": 0, "right": 0, "left": 0, "back": 0, "bottom": 0}

    def roll(self, direction):
        self.direction = direction
        if self.direction == "N":
            w = self.side["top"]
            self.side["top"] = self.side["front"]
            self.side["front"] = self.side["bottom"]
            self.side["bottom"] = self.side["back"]
            self.side["back"] = w
        elif self.direction == "S":
            w = self.side["top"]
            self.side["top"] = self.side["back"]
            self.side["back"] = self.side["bottom"]
            self.side["bottom"] = self.side["front"]
            self.side["front"] = w
        elif self.direction == "E":
            w = self.side["top"]
            self.side["top"] = self.side["left"]
            self.side["left"] = self.side["bottom"]
            self.side["bottom"] = self.side["right"]
            self.side["right"] = w
        elif self.direction == "W":
            w = self.side["top"]
            self.side["top"] = self.side["right"]
            self.side["right"] = self.side["bottom"]
            self.side["bottom"] = self.side["left"]
            self.side["left"] = w

dice = Dice()
for s, n in zip(dice.side, input().split()):
    dice.side[s] = n

for direction in input():
    dice.roll(direction)
print(dice.side["top"])

