class Dice:
  def __init__(self, state):
    self.state = state

  def vertical(self, direction):
    s = self.state
    state = [s[1], s[5], s[0], s[4]]
    if direction < 0:
      s[0], s[1], s[4], s[5] = state
    elif 0 < direction:
      s[0], s[1], s[4], s[5] = reversed(state)
    return self
  
  def lateral(self, direction):
    s = self.state
    state = [s[2], s[5], s[0], s[3]]
    if direction < 0:
      s[0], s[2], s[3], s[5] = state
    elif 0 < direction:
      s[0], s[2], s[3], s[5] = reversed(state)
    return self

  def north(self):
    self.vertical(-1)
    return self

  def south(self):
    self.vertical(1)
    return self
  
  def east(self):
    self.lateral(1)
    return self

  def west(self):
    self.lateral(-1)
    return self

init_state = input().split()

for i in range(int(input())):
  dice = Dice(init_state)
  up, front = input().split()

  if up == dice.state[0] \
    and front == dice.state[1]:
      print(dice.state[2])
  else:
    for c in list('NNNNWNNNWNNNENNNENNNWNNN'):       
      if c == 'N':
        dice.north()
      elif c == 'S':
        dice.south()
      elif c == 'W':
        dice.west()
      elif c == 'E':
        dice.east()
      if up == dice.state[0] \
        and front == dice.state[1]:
          print(dice.state[2])
          break

