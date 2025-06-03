str = input()
while not str == '-':
  n = int(input())
  for i in range(n):
    h = int(input())
    str = str[h:] + str[:h]
  print(str)
  str = input() 