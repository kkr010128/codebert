input = raw_input()

for i in xrange(len(input)):
  # print "i = " + str(i) + ", input[i] = " + input[i]
  if input[i].islower():
    input = input[:i] + input[i].upper() + input[i + 1:]
  elif input[i].isupper():
    input = input[:i] + input[i].lower() + input[i + 1:]

print input