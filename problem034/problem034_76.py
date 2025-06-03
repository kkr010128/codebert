import random

class Dice:
  def __init__(self, list = map(str, range(1, 7))):
    self.top = list[0]
    self.front = list[1]
    self.right = list[2]
    self.left = list[3]
    self.back = list[4]
    self.bottom = list[5]

  def print_all(self):
    print "top = " + self.top
    print "front = " + self.front
    print "right = " + self.right
    print "left = " + self.left
    print "back = " + self.back
    print "bottom = " + self.bottom

  def roll_N(self):
    temp = self.top
    self.top = self.front
    self.front = self.bottom
    self.bottom = self.back
    self.back = temp

  def roll_S(self):
    temp = self.top
    self.top = self.back
    self.back = self.bottom
    self.bottom = self.front
    self.front = temp

  def roll_W(self):
    temp = self.top
    self.top = self.right
    self.right = self.bottom
    self.bottom = self.left
    self.left = temp

  def roll_E(self):
    temp = self.top
    self.top = self.left
    self.left = self.bottom
    self.bottom = self.right
    self.right = temp

  def random_roll(self):
    ram = random.randint(1, 4)
    if ram == 1:
      self.roll_E()
    elif ram == 2:
      self.roll_N()
    elif ram == 3:
      self.roll_S()
    else:
      self.roll_W()

my_dice = Dice(raw_input().split(" "))
q = int(raw_input())

for i in xrange(q):
  input_dice = raw_input().split(" ")
  while True:
    if my_dice.top == input_dice[0] and my_dice.front == input_dice[1]:
      break
    else:
      my_dice.random_roll()
  print my_dice.right