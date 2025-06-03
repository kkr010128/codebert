import sys 
dataset = sys.stdin.readlines()

for s in range(ord('a'), ord('z') + 1):
 count = 0
 for data in dataset:
  count += data.lower().count(chr(s))
 print("{0} : {1}".format(chr(s), count))