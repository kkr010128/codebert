class Dice:
  def __init__(self):
    self.top = 1
    self.front = 2
    self.left = 4

  @property
  def bottom(self):
    return 7 - self.top

  @property
  def back(self):
    return 7 - self.front

  @property
  def right(self):
    return 7 - self.left

  def move(self, direction):
    if direction == 'N':
      bottom = self.bottom
      self.top = self.front
      self.front = bottom
    elif direction == 'W':
      right = self.right
      self.left = self.top
      self.top = right
    elif direction == 'E':
      bottom = self.bottom
      self.top = self.left
      self.left = bottom
    elif direction == 'S':
      back = self.back
      self.front = self.top
      self.top = back

  def __repr__(self):
    print(self.__dict__)

dice = Dice()
numbers = input().split()
for cmd in input():
  dice.move(cmd)
print(numbers[dice.top - 1])