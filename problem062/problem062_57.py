while True:
  input = raw_input()
  if input == "0":
    break
  sum = 0
  for i in xrange(len(input)):
    sum += int(input[i])
  print sum