import sys
buff=sys.stdin.read()
buff=buff.lower()
alp="abcdefghijklmnopqrstuvwxyz"
for i in range(len(alp)):
  print(alp[i],':',buff.count(alp[i]))
