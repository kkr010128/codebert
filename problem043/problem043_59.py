list = []
while True:
  line = raw_input().split(" ")
  if line[0] == "0" and line[1] == "0":
    break
  line = map(int, line)
  #print line
  if line[0] > line[1]:
    temp = line[0]
    line[0] = line[1]
    line[1] = temp
  print " ".join(map(str, line))