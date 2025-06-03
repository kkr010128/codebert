SW = input()
SW = [int(i) for i in list(SW.split())]

if SW[0]<=SW[1]:
  print('unsafe')
else:
  print('safe')