A = input()
A = list(A.split())
sum = 0

for i in A:
  sum += int(i)

if sum >= 22:
  print('bust')
else:
  print('win')