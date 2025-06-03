a,b,c,d = list(map(int,input().split()))

t_win_turn = c // b
if c % b > 0:
  t_win_turn += 1

a_win_turn = a // d
if a % d > 0:
  a_win_turn += 1

if t_win_turn <= a_win_turn:
  print('Yes')
else:
  print('No')
