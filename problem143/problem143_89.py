n = int(input())
p = input()

if n>=len(p):
  print(p)
else:
  print(p[:n] + '...')