class Stack:
  def __init__(self):
    self.count = 1
    self.lst = []
  
  def push(self, element):
    if element == self.count:
      self.lst.append(element)
      self.count += 1
  
  def length(self):
    return len(self.lst)

n = int(input())
a = list(map(int, input().split()))
stack = Stack()
for i in a:
  stack.push(i)

b = stack.length()
if b == 0:
  print('-1')
else:
  print(n - b)
