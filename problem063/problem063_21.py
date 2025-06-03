import sys

dic = {}
for i in xrange(97, 123):
  dic.setdefault(chr(i), 0)

line = ""
while True:
  try:
    temp = raw_input()
    # print "temp = " + temp
    if temp != "":
      line += temp
    else:
      break
  except:
    break

# print line

for i in xrange(len(line)):
  try:
    if line[i].lower() in dic:
      dic[line[i].lower()] += 1
  except TypeError:
    continue

  # print dic
for i in xrange(97, 123):
  print chr(i) + " : " + str(dic[chr(i)])