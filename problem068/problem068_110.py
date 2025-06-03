str0 = raw_input()
q = int(raw_input())

for i in xrange(q):
  # print "###########################"
  # print "str0 = " + str0
  line = raw_input().split(" ")
  temp = str0[int(line[1]):int(line[2])+1]
  if line[0] == "print":
    print temp
  elif line[0] == "reverse":
    temp2 = [] 
    # print "temp = " + temp
    for j in xrange(len(temp)):
      temp2.append(temp[len(temp) - j - 1])
    str0 = str0[:int(line[1])] + "".join(temp2) + str0[int(line[2]) + 1:]
    # print "str0 = " + str0
  elif line[0] == "replace":
    str0 = str0[:int(line[1])] + line[3] + str0[int(line[2]) + 1:]
    # print "str0 = " + str0