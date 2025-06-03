class Dice:
  def make_dice(self, value):
    self.face = value
  def move(self, direc):
    if direc == "N":
      self.face = [self.face[1], self.face[5], self.face[2], self.face[3], self.face[0], self.face[4]]
      return self.face
    elif direc == "E":
      self.face = [self.face[3], self.face[1], self.face[0], self.face[5], self.face[4], self.face[2]]
      return self.face
    elif direc == "S":
      self.face = [self.face[4], self.face[0], self.face[2], self.face[3], self.face[5], self.face[1]]
      return self.face
    elif direc == "W":
      self.face = [self.face[2], self.face[1], self.face[5], self.face[0], self.face[4], self.face[3]]
      return self.face
  def get_face(self, top):
    if top == self.face[0]:
      return self.face
    elif top == self.face[1]:
      return dice.move("N")
    elif top == self.face[2]:
      return dice.move("W")
    elif top == self.face[3]:
      return dice.move("E")
    elif top == self.face[4]:
      return dice.move("S")
    elif top == self.face[5]:
      dice.move("N")
      return dice.move("N")
  def right_face(self, face1, face2):
    if face2 == self.face[1]:
      return self.face[2]
    elif face2 == self.face[2]:
      return self.face[4]
    elif face2 == self.face[4]:
      return self.face[3]
    elif face2 == self.face[3]:
      return self.face[1]

num = list(map(int, input().split()))
q = int(input())
dice = Dice()
for i in range(q):
  dice.make_dice(num)
  f1, f2 = map(int,input().split())
  dice.get_face(f1)
  print(dice.right_face(f1,f2))
