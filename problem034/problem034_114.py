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
n = int(input())
for i in range(n):
    (face1, face2) = map(int, input().split())
    if face2 == dice.number(3) or face2 == dice.number(4):
        dice.roll_west()
    while dice.number(2) != face2:
        dice.roll_north()
    while dice.number(1) != face1:
        dice.roll_west()
    print(dice.number(3))