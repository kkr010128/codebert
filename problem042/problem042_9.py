list = []
while True:
  line = raw_input()
  list.append(line)
  if line == "0":
    break

i = 0
for x in list[:-1]:
  i += 1
  print "Case %d: %s" % (i, x)