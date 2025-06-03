class Dice:

    def __init__(self, faces):
        self.faces = tuple(faces)

    def roll_north(self):
        self.faces = (self.faces[1], self.faces[5], self.faces[2],
                      self.faces[3], self.faces[0], self.faces[4])

    def roll_south(self):
        self.faces = (self.faces[4], self.faces[0], self.faces[2],
                      self.faces[3], self.faces[5], self.faces[1])

    def roll_west(self):
        self.faces = (self.faces[2], self.faces[1], self.faces[5],
                      self.faces[0], self.faces[4], self.faces[3])

    def roll_east(self):
        self.faces = (self.faces[3], self.faces[1], self.faces[0],
                      self.faces[5], self.faces[4], self.faces[2])

    def number(self, face_id):
        return self.faces[face_id - 1]


dice = Dice(list(map(int, input().split())))
commands = input()

for c in commands:
    if c == "N":
        dice.roll_north()
    elif c == "S":
        dice.roll_south()
    elif c == "W":
        dice.roll_west()
    elif c == "E":
        dice.roll_east()
print(dice.number(1))