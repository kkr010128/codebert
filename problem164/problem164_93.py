A, B, C, D = map(int, input().split())
takahashi_hp = A 
aoki_hp = C
while True:
  aoki_hp -= B
  if aoki_hp <= 0:
    break
  takahashi_hp -= D
  if takahashi_hp <= 0:
    break
if takahashi_hp <= 0:
  print("No")
else:
  print("Yes")