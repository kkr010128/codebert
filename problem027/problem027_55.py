import math

def koch_kurve(n, p1=[0, 0], p2=[100, 0]):
  if n == 0: return

  s, t, u = make_edge_list(p1, p2)

  koch_kurve(n-1, p1, s)
  # print(s)
  # print(s)
  print(" ".join([ str(i) for i in s ]))
  koch_kurve(n-1, s, u)
  print(" ".join([ str(i) for i in u ]))
  koch_kurve(n-1, u, t)
  print(" ".join([ str(i) for i in t ]))
  koch_kurve(n-1, t, p2)


def make_edge_list(p1, p2):
  sx = 2 / 3 * p1[0] + 1 / 3 * p2[0]
  sy = 2 / 3 * p1[1] + 1 / 3 * p2[1]
  # s = (sx, sy)
  s = [sx, sy]

  tx = 1 / 3 * p1[0] + 2 / 3 * p2[0]
  ty = 1 / 3 * p1[1] + 2 / 3 * p2[1]
  t = [tx, ty]

  theta = math.radians(60)
  ux = math.cos(theta) * (tx - sx) - math.sin(theta) * (ty - sy) + sx
  uy = math.sin(theta) * (tx - sx) + math.cos(theta) * (ty - sy) + sy
  u = [ux, uy]

  return s, t, u

n = int(input())
print("0 0")
koch_kurve(n)
print("100 0")


