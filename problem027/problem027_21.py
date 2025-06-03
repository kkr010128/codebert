  
import math

class Pos:
  def init(x, y):
    self.x = x
    self.y = y

def kock(n, p1, p2):
  if n == 0: return

  s, t = Pos(), Pos()
  s.x = (2 * p1.x + 1 * p2.x) / 3
  s.y = (2 * p1.y + 1 * p2.y) / 3
  t.x = (1 * p1.x + 2 * p2.x) / 3
  t.y = (1 * p1.y + 2 * p2.y) / 3

  cos60 = math.cos(math.radians(60))
  sin60 = math.sin(math.radians(60))

  u = Pos()
  u.x = (t.x - s.x) * cos60 - (t.y - s.y) * sin60 + s.x
  u.y = (t.x - s.x) * sin60 + (t.y - s.y) * cos60 + s.y

  kock(n-1, p1, s)
  print("{:.5f} {:.5f}".format(s.x, s.y))
  kock(n-1, s, u)
  print("{:.5f} {:.5f}".format(u.x, u.y))
  kock(n-1, u, t)
  print("{:.5f} {:.5f}".format(t.x, t.y))
  kock(n-1, t, p2)

n = int(input())

p1, p2 = Pos(), Pos()
p1.x, p1.y = 0.0, 0.0
p2.x, p2.y = 100.0, 0.0

print("{:.5f} {:.5f}".format(p1.x, p1.y))
kock(n, p1, p2)
print("{:.5f} {:.5f}".format(p2.x, p2.y))
