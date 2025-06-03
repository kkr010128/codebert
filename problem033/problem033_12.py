class Dice:
  __x = 1
  __y = 0
  def __init__(self,dice):
    self.dice = dice
    
  def output(self):
    print(self.dice[0])
    
  def move(self,str):
    if str == 'N':
      temp = self.dice[0]
      self.dice[0] = self.dice[1]
      self.dice[1] = self.dice[5]
      self.dice[5] = self.dice[4]
      self.dice[4] = temp
    elif str == 'S':
      temp = self.dice[0]
      self.dice[0] = self.dice[4]
      self.dice[4] = self.dice[5]
      self.dice[5] = self.dice[1]
      self.dice[1] = temp

    elif str == 'E':
      temp = self.dice[0]
      self.dice[0] = self.dice[3]
      self.dice[3] = self.dice[5]
      self.dice[5] = self.dice[2]
      self.dice[2] = temp
      
    elif str == 'W':
      temp = self.dice[0]
      self.dice[0] = self.dice[2]
      self.dice[2] = self.dice[5]
      self.dice[5] = self.dice[3]
      self.dice[3] = temp      
      
di = list(map(int,input().split()))
m = list(input())
di = Dice(di)
for i in m:
  di.move(i)
di.output()

