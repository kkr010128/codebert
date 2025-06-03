N = int(input())
pi = 360
while True:
  if pi % N == 0:
    print(pi//N)
    exit()
  else:
    pi+=360