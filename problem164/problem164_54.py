A, B, C, D = map(int, input().split())
def battle(x_hp, x_atk, y_hp, y_atk):
  turn = 0
  while 1:
    if turn == 0:
      y_hp -= x_atk
      if y_hp < 1:
        return "Yes"
    else:
      x_hp -= y_atk
      if x_hp < 1:
        return "No"
    turn = 1 - turn
print(battle(A, B, C, D))