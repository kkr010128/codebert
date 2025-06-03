class Dice:
    def __init__(self,faces):
        self.faces = tuple(faces)
    def N(self):
        self.faces = (self.faces[1], self.faces[5], self.faces[2],
                      self.faces[3], self.faces[0], self.faces[4])
    def S(self):
        self.faces = (self.faces[4], self.faces[0], self.faces[2],
                      self.faces[3], self.faces[5], self.faces[1])
    def W(self):
        self.faces = (self.faces[2], self.faces[1], self.faces[5],
                      self.faces[0], self.faces[4], self.faces[3])
    def E(self):
        self.faces = (self.faces[3], self.faces[1], self.faces[0],
                      self.faces[5], self.faces[4], self.faces[2])
    def number(self, face_id):
        return self.faces[face_id - 1]
dice = Dice(list(map(int, input().split())))
x=input()
 
for i in x:
    if i == "N":
        dice.N()
    elif i == "S":
        dice.S()
    elif i == "W":
        dice.W()
    elif i == "E":
        dice.E()
print(dice.number(1))