from sys import stdin
S = stdin.readline().rstrip()
pattern = ['hi', 'hihi', 'hihihi', 'hihihihi', 'hihihihihi']
if S in pattern:
  print('Yes')
else:
  print('No')