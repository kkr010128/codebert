n = int(input())
plus_bracket = []
minus_bracket = []

for _ in range(n):
  mini = 0
  cur = 0
  for bracket in input():
    if bracket == '(':
      cur += 1
    else:
      cur -= 1
    if cur < mini:
      mini = cur
  if cur > 0:
    plus_bracket.append([-mini, cur])
  else:
    minus_bracket.append([cur - mini, -cur])

success = True
cur = 0
plus_bracket.sort()
minus_bracket.sort()
for bracket in plus_bracket:
  if cur < bracket[0]:
    success = False
    break
  cur += bracket[1]
back_cur = 0
for bracket in minus_bracket:
  if back_cur < bracket[0]:
    success = False
    break
  back_cur += bracket[1]
if cur != back_cur:
  success = False

if success:
  print('Yes')
else:
  print('No')