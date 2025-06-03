input = raw_input().split(" ")
a = int(input[0])
b = int(input[1])
c = int(input[2])

if a < b:
  if b < c:
    print "Yes"
  else:
    print "No"
else:
  print "No"