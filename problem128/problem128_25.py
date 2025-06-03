def p_has_value_x(p:list, x:int):
  for item in p:
    if int(item) == x:
      return True
  return False

def solve(p: list, x:int) -> int:
  if not p_has_value_x(p, x):
    return x

  pos = 1
  while True:
    aim_value = x - pos
    if aim_value <= 0:
      return aim_value
    if not p_has_value_x(p, aim_value):
      return aim_value
    aim_value = x + pos
    if not p_has_value_x(p, aim_value):
      return aim_value
    pos += 1


x, n = map(int, input().split())

if n == 0:
  print(x)
else:
  p = input().split()
  print(solve(p, x))
