table = [0] * 26
string = []
while True:
  try:
    string += list(input())
  except EOFError:
    break

for s in string:
  n = ord(s.lower()) - 97
  if n >= 0 and n <= 25:
    table[n] += 1

for idx, s in enumerate(table):
  print(chr(idx + 97) + " : " + str(s))
