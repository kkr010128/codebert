class Dice:
  def __init__(self, list1):
    self.f = list1
  def move(self, direct):
    if direct == "N":
        self.f[0], self.f[1], self.f[4], self.f[5] = self.f[1], self.f[5], self.f[0], self.f[4]
        return self.f
    elif direct == "E":
        self.f[0], self.f[2], self.f[3], self.f[5] = self.f[3], self.f[0], self.f[5], self.f[2]
        return self.f
    elif direct == "S":
         self.f[0], self.f[1], self.f[4], self.f[5] = self.f[4], self.f[0], self.f[5], self.f[1]
         return self.f
    elif direct == "W":
        self.f[0], self.f[2], self.f[3], self.f[5] = self.f[2], self.f[5], self.f[0], self.f[3]
        return self.f

data = list(map(int, input().split()))
direction = input()
dice = Dice(data)
for i in direction:
  dice.move(i)
print(dice.f[0])
