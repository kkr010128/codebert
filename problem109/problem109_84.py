n = int(input())
lst = [0] *4

for i in range(n):
  a = input()
  if a == 'AC':
    lst[0] += 1
  if a == 'WA':
    lst[1] += 1
  if a == 'TLE':
    lst[2] += 1
  if a == 'RE':
    lst[3] += 1
    
print('AC x',lst[0])
print('WA x',lst[1])
print('TLE x',lst[2])
print('RE x',lst[3])